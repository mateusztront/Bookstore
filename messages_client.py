from connection import connect
from models import Message

conn = connect()
cursor = conn.cursor()

while True:
    x = input("""Choose an option:
    1 - show all messages
    2 - send message
    """)

    if int(x) == 1:
        for message in Message.load_all_messages(cursor):
            print(message.id, message.from_id, message.to_id, message.text, message.creation_date)

    if int(x) == 2:
        receiver = input("To whom you want to send message? enter id")
        sender = input("Your id")
        text = input("text of message")
        new_message = Message(receiver, sender, text)
        new_message.save_to_db(cursor)


