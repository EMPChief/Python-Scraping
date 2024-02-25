import sqlite3

class Database:
    def __init__(self, db_name=None, tb=None):
        self.connection = sqlite3.connect(db_name)
        self.cursor = self.connection.cursor()
        self.tb = tb
    
    def create_table(self):
        self.cursor.execute(f"CREATE TABLE IF NOT EXISTS {self.tb} (id INTEGER PRIMARY KEY, band TEXT, venue TEXT, date TEXT)")
    
    def insert_many_rows(self, rows):
        placeholders = ','.join(['?']*len(rows[0]))
        self.cursor.executemany(f"INSERT INTO {self.tb} VALUES ({placeholders})", rows)
        self.connection.commit()
        
    def insert_one_row(self, row):
        placeholders = ','.join(['?']*len(row))
        self.cursor.execute(f"INSERT INTO {self.tb} VALUES ({placeholders})", row)
        self.connection.commit()
    
    def select_all_data(self):
        self.cursor.execute(f"SELECT * FROM {self.tb}")
        data = self.cursor.fetchall()
        return data

    
    def close_connection(self):
        self.connection.close()


db = Database(db_name='database.db', tb='tourevent')
db.create_table()

new_rows = [
    ('2024-02-25 17:19:59', 'The Rolling Stones', 'The Forum', '1975.07.11'),
    ('2024-02-25 17:19:59', 'The Rolling Stones', 'Madison Square Garden', '1969.11.28'),
    ('2024-02-25 17:19:59', 'The Rolling Stones', 'Hyde Park', '1969.07.05'),
    ('2024-02-25 17:19:59', 'Pink Floyd', 'Earls Court Exhibition Centre', '1980.08.09'),
    ('2024-02-25 17:19:59', 'Pink Floyd', 'Pompeii Amphitheatre', '1971.10.04'),
    ('2024-02-25 18:19:59', 'Pink Floyd', 'Rainbow Theatre', '1972.02.20'),
    ('2024-02-25 18:19:59', 'AC/DC', 'Donington Park', '1991.08.17'),
    ('2024-02-25 18:29:59', 'AC/DC', 'River Plate Stadium', '2009.12.04'),
    ('2024-02-25 19:29:59', 'AC/DC', 'Hammersmith Odeon', '1979.11.02'),
    ('2024-02-25 19:39:59', 'The Beatles', 'The Ed Sullivan Show', '1964.02.09'),
    ('2024-02-25 19:39:59', 'The Beatles', 'The Ed Sullivan Show', '1964.02.16'),
    ('2024-02-25 19:39:59', 'The Beatles', 'The Ed Sullivan Show', '1964.07.13'),
    ('2024-02-25 19:49:59', 'Led Zeppelin', 'Madison Square Garden', '1973.07.27'),
    ('2024-02-25 19:49:59', 'Led Zeppelin', 'Knebworth Festival', '1979.08.04'),
    ('2024-02-25 20:49:59', 'Led Zeppelin', 'Royal Albert Hall', '1970.0.09'),
    ('2024-02-25 21:59:59', 'Queen', 'Wembley Stadium', '1986.07.12'),
    ('2024-02-25 22:59:59', 'Queen', 'Rock in Rio', '1985.01.12'),
    ('2024-02-25 23:59:59', 'Queen', 'Live Aid', '1985.07.13'),
]

db.insert_many_rows(new_rows)

data = db.select_all_data()
print(data)

db.close_connection()
