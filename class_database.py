import sqlite3

class Database:
    def __init__(self, db_name=None, tb=None):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.tb = tb
    
    def create_table(self):
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.tb} (id INTEGER PRIMARY KEY, band TEXT, venue TEXT, date TEXT)")
    
    def insert_many_rows(self, rows):
        self.cursor.executemany("INSERT INTO {self.tb} VALUES(?,?,?,?)", rows)
        self.connection.commit()
    
    def select_all_data(self):
        self.cursor.execute(f"SELECT * FROM {self.tb}")
        data = self.cursor.fetchall()
        return data

    
    def close_connection(self):
        self.connection.close()


db = Database(db_name='database.db', tb='tourevent')
db.create_table()

"""new_rows = [
    ('2024-02-25 17:19:59', 'The Rolling Stones', 'The Forum', '1975.07.11'),
    ('2024-02-25 17:19:59', 'The Rolling Stones', 'Madison Square Garden', '1969.11.28'),
]
db.insert_rows(new_rows)"""

data = db.select_all_data()
print(data)

db.close_connection()
