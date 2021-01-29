from hashing import hash_password


class User:

    def __init__(self, username="", password="", salt=""):

        self._id = None
        self.username = username
        self._password = hash_password(password, salt)

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

    #@staticmethod # czy to na pewno powinno tu być?
    def save_to_db(self, cursor):
        if self._id == None:
            sql = f"""INSERT INTO users(username, hashed_password)
                            VALUES({self.username}, {self.hashed_password}) RETURNING id"""
            cursor.execute(sql)
            self._id = cursor.fetchone()[0]  # or cursor.fetchone()['id']
            return True
        return False


balwan = User("mateusztront", "qwe123")
balwan.save_to_db(cursor)