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
    
    def delete_data(self, condition):
        self.cursor.execute(f"DELETE FROM {self.tb} WHERE {condition}")
        self.connection.commit()
    
    def drop_table(self):
        self.cursor.execute(f"DROP TABLE {self.tb}")
        self.connection.commit()

    def close_connection(self):
        self.connection.close()


if __name__ == '__main__':
    columns = ['id INTEGER PRIMARY KEY', 'band TEXT', 'venue TEXT', 'date TEXT']
    db = Database(db_name='database.db', tb='tourevent')
    db.create_table(columns)
    new_rows = [
        ('2024-02-25 17:19:59', 'The Rolling Stones', 'The Forum', '1975.07.11'),
        ('2024-02-25 17:20:00', 'The Rolling Stones', 'The Forum', '1975.07.11'),
    ]
    db.insert_many_rows(new_rows)
    db.delete_data("city='The Forum'")
    data = db.select_all_data()
    print(data)
    db.close_connection()
