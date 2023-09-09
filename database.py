import sqlite3


class Connector:
    def __init__(self):
        self.connect = sqlite3.connect('myDatabase.db')
        self.cursor = self.connect.cursor()
        self.create_user_table()

    def create_user_table(self):
        with self.connect:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                first_name TEXT,
                last_name TEXT
            )""")

    def create_admin(self):
        with self.connect:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                first_name TEXT,
                last_name TEXT
            )""")


db = Connector()
