import sqlite3


class Connector:
    def __init__(self):
        self.connect = sqlite3.connect('myDatabase.db')
        self.cursor = self.connect.cursor()
        self.create_user_table()
        self.create_admin_table()

    def create_user_table(self):
        with self.connect:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                first_name TEXT,
                last_name TEXT
            )""")

    def create_admin_table(self):
        with self.connect:
            self.cursor.execute("""CREATE TABLE IF NOT EXISTS users(
                first_name TEXT,
                last_name TEXT
            )""")

    def add_user(self, firstname, lastname):
        with self.connect:
            self.cursor.execute("""INSERT INTO users(first_name, last_name) VALUES (:first_name, :last_name)""",
                                {'first_name': firstname, 'last_name': lastname})


db = Connector()
