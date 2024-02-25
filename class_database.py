import sqlite3


class Database:
    def __init__(self, db_name=None, tb=None):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.tb = tb

    def create_table(self, columns):
        columns_str = ', '.join(columns)
        self.cursor.execute(
            f"CREATE TABLE IF NOT EXISTS {self.tb} ({columns_str})")

    def insert_many_rows(self, rows):
        placeholders = ','.join(['?']*len(rows[0]))
        existing_rows = self.select_all_data()

        filtered_rows = [row for row in rows if row not in existing_rows]

        self.cursor.executemany(
            f"INSERT INTO {self.tb} VALUES ({placeholders})", filtered_rows)
        self.connection.commit()

    def insert_one_row(self, row):
        placeholders = ','.join(['?']*len(row))
        existing_rows = self.select_all_data()
        if row not in existing_rows:
            self.cursor.execute(
                f"INSERT INTO {self.tb} VALUES ({placeholders})", row)
            self.connection.commit()
        else:
            print("Row already exists, skipping insertion.")

    def select_all_data(self):
        self.cursor.execute(f"SELECT * FROM {self.tb}")
        data = self.cursor.fetchall()
        return data
    
    def select_one_data(self, condition):
        self.cursor.execute(f"SELECT * FROM {self.tb} WHERE {condition}")
        data = self.cursor.fetchone()
        return data
    
    def update_data(self, condition, new_data):
        self.cursor.execute(
            f"UPDATE {self.tb} SET {new_data} WHERE {condition}")
        self.connection.commit()
        return data
    
    def delete_data(self, condition):
        self.cursor.execute(f"DELETE FROM {self.tb} WHERE {condition}")
        self.connection.commit()
        return data
    
    def drop_table(self):
        self.cursor.execute(f"DROP TABLE {self.tb}")
        self.connection.commit()

    def close_connection(self):
        self.connection.close()


columns = ['id INTEGER PRIMARY KEY', 'band TEXT', 'venue TEXT', 'date TEXT']

db = Database(db_name='database.db', tb='tourevent')
db.create_table(columns)

new_rows = [
    ('2024-02-25 17:19:59', 'The Rolling Stones', 'The Forum', '1975.07.11'),
    ('2024-02-25 17:19:59', 'The Rolling Stones',
     'Madison Square Garden', '1969.11.28'),
    ('2024-02-25 17:19:59', 'The Rolling Stones', 'The Forum', '1975.07.11'),
    ('2024-02-25 18:30:00', 'Pink Floyd', 'Earls Court Exhibition Centre', '1980.08.09'),
    ('2024-02-25 18:30:00', 'Pink Floyd', 'Pompeii Amphitheatre', '1971.10.04'),
    ('2024-02-25 18:30:00', 'Led Zeppelin', 'Madison Square Garden', '1973.07.27'),
    ('2024-02-25 18:30:00', 'Queen', 'Wembley Stadium', '1986.07.12'),
    ('2024-02-25 18:30:00', 'AC/DC', 'River Plate Stadium', '2009.12.04'),
    ('2024-02-25 18:30:00', 'The Beatles', 'The Ed Sullivan Show', '1964.02.09')
]


db.insert_many_rows(new_rows)

data = db.select_all_data()
print(data)

db.close_connection()
