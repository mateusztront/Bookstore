from connection import connect
from create import create_db, create_table
from models import User
from tables import users_columns, messages_columns
from psycopg2 import OperationalError, errorcodes, errors

conn = connect()
cursor = conn.cursor()

try:
    create_db('bookstore')
    create_table('users', users_columns)
    create_table('messages', messages_columns)
except:
    print("błąd z tworzeniem db lub tabel")

while True:
    x = input("""Choose an option:
    1 - create user
    2 - change password
    3 - delete user
    4 - list users
    5 - help 
    """)

    if int(x) == 1:
        name = input("Type user name")
        password = input("Type password")
        new_user = User(name, password)
        try:
            new_user.save_to_db(cursor)
        # except errors.UniqueViolation as err:
        # print_psycopg2_exception(err)
        except:
            print("błąd z dodaniem użytkownika")

    if int(x) == 2:
        name = input("Type user name")
        #trzeba by sprawdzić czy stare pass rowna sie z nowo podanym
        new_pass = input("Type new password")
        user_temp = User.load_user_by_username(cursor, name)
        user_temp.hashed_password = new_pass
        print(user_temp.hashed_password)
        try:
            user_temp.save_to_db(cursor)
            print("Password changed")
        # except errors.UniqueViolation as err:
        # print_psycopg2_exception(err)
        except:
            print("błąd ze zmiana hasla")

    if int(x) == 3:
        name = input("Type user name")
        # trzeba by sprawdzić czy stare pass rowna sie z nowo podanym
        user_temp = User.load_user_by_username(cursor, name)
        try:
            user_temp.delete(cursor)
            print(f"User {user_temp.username} has been deleted")
        except:
            print("błąd usuwania")

    if int(x) == 4:
        for user in User.load_all_users(cursor):
            print(user.username)

    if int(x) == 5:
        print("Choose one another option")


