from connection import connect
from hashing import hash_password


class User:

    def __init__(self, username="", password="", salt=""):
        self._id = None
        self.username = username
        self._hashed_password = hash_password(password, salt)

    @property
    def id(self):
        return self._id

    @property
    def hashed_password(self):
        return self._hashed_password

    def set_password(self, password, salt=""):
        self._hashed_password = hash_password(password, salt)

    @hashed_password.setter
    def hashed_password(self, password):
        self.set_password(password)


    def save_to_db(self, cursor):
        if self._id == None:
            sql = f"""INSERT INTO users(username, hashed_password)
                            VALUES ('{self.username}', '{self.hashed_password}') RETURNING id"""
            cursor.execute(sql)
            self._id = cursor.fetchone()[0]  # or cursor.fetchone()['id']
            return True
        else:
            sql = f"""UPDATE users SET hashed_password = '{self.hashed_password}' WHERE id = {self._id}"""
            cursor.execute(sql)
        return True




# conn = connect()
# cursor = conn.cursor()
# balwan = User("mateusztront", "qwe123")
# balwan.save_to_db(cursor)


    @staticmethod
    def load_user_by_id(cursor, id_):
        sql = f"SELECT id, username, hashed_password FROM users WHERE id={id_}"
        cursor.execute(sql, (id_,))  # (id_, ) - cause we need a tuple
        data = cursor.fetchone()
        if data:
            id_, username, hashed_password = data
            loaded_user = User(username)
            loaded_user._id = id_
            loaded_user._hashed_password = hashed_password
            return loaded_user
        else:
            return None

# conn = connect()
# cursor = conn.cursor()
# moje = User.load_user_by_id(cursor, 2)
# print(moje._hashed_password)

    @staticmethod
    def load_user_by_username(cursor, username):
        sql = f"SELECT id, username, hashed_password FROM users WHERE username='{username}'"
        cursor.execute(sql, (username,))  # (id_, ) - cause we need a tuple
        data = cursor.fetchone()
        if data:
            id_, username, hashed_password = data
            loaded_user = User(username)
            loaded_user._id = id_
            loaded_user._hashed_password = hashed_password
            return loaded_user
        else:
            return None





    @staticmethod
    def load_all_users(cursor):
        sql = "SELECT id, username, hashed_password FROM Users"
        users = []
        cursor.execute(sql)
        for row in cursor.fetchall():
            id_, username, hashed_password = row
            loaded_user = User()
            loaded_user._id = id_
            loaded_user.username = username
            loaded_user._hashed_password = hashed_password
            users.append(loaded_user)
        return users

# conn = connect()
# cursor = conn.cursor()
# for user in User.load_all_users(cursor):
#     print(user.username)




    def delete(self, cursor):
        sql = f"DELETE FROM Users WHERE id={self.id}"
        cursor.execute(sql)
        self._id = None
        return True



# conn = connect()
# cursor = conn.cursor()
# uzer = User.load_user_by_id(cursor, 2)
# User.delete(uzer, cursor)

# conn = connect()
# cursor = conn.cursor()
# moje = User.load_user_by_username(cursor, 'wojtekszczesniak')
# print(moje._hashed_password)

# conn = connect()
# cursor = conn.cursor()
# gosia = User("gosia", "1234")
# gosia.save_to_db(cursor)

class Message:

    def __init__(self, from_id="", to_id="", text=""):
        self.to_id = to_id
        self.from_id = from_id
        self.text = text
        self.creation_data = None
        self._id = None

    @property
    def id(self):
        return self._id

    def save_to_db(self, cursor):
        if self._id == None:
            sql = f"""INSERT INTO messages(from_id, to_id, text)
                            VALUES ('{self.from_id}', '{self.to_id}', '{self.text}') RETURNING id"""
            cursor.execute(sql)
            self._id = cursor.fetchone()[0]  # or cursor.fetchone()['id']
            return True
        return False



    @staticmethod
    def load_all_messages(cursor):
        messeges = []
        sql = f"""
        SELECT id, from_id, to_id, text, creation_date FROM messages
        """
        cursor.execute(sql)
        for row in cursor.fetchall():
            _id, from_id, to_id, text, creation_date = row
            loaded_message = Message()
            loaded_message._id = _id
            loaded_message.from_id = from_id
            loaded_message.to_id = to_id
            loaded_message.text = text
            loaded_message.creation_date = creation_date
            messeges.append(loaded_message)
        return messeges

# conn = connect()
# cursor = conn.cursor()
# wiadomosc1 = Message('1', '2', 'Życzę miłego dnia')
# wiadomosc1.save_to_db(cursor)

# conn = connect()
# cursor = conn.cursor()
# for message in Message.load_all_messages(cursor):
#      print(message.text)