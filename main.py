from connection import connect
from create import create_db, create_table
from models import User
from tables import users_columns, messages_columns

while True:
    try:
        create_db('bookstore')
        create_table('users', users_columns)
        create_table('messages', messages_columns)
    except:
        print("błąd z tworzeniem db lub tabel")

    x = input("""Choose an option:
    1 - create user
    2 - change password
    3 - delete user
    4 - list users
    5 - help 
    """)

    conn = connect()
    cursor = conn.cursor()

    if x == 1:
        name = input("Type user name")
        password = input("Type password")
        try