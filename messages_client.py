

conn = connect()
cursor = conn.cursor()

while True:
    x = input("""Choose an option:
    1 - show all messages
    2 - send message
    """)

    if int(x) == 1:
        for message in Message.load_all_messages()