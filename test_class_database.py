import unittest
from dbs.class_database import Database


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.db = Database(db_name='test_database.db', tb='test_table')
        self.columns = ['id INTEGER PRIMARY KEY', 'name TEXT', 'age INTEGER']

    def tearDown(self):
        self.db.close_connection()

    def test_create_table(self):
        self.db.create_table(self.columns)
        # Assert that the table is created successfully
        self.assertIn('test_table', self.db.cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table'").fetchall())

    def test_insert_one_row(self):
        row = (1, 'John Doe', 25)
        self.db.create_table(self.columns)
        self.db.insert_one_row(row)
        # Assert that the row is inserted successfully
        self.assertIn(row, self.db.select_all_data())

    def test_insert_many_rows(self):
        rows = [
            (2, 'Jane Smith', 30),
            (3, 'Bob Johnson', 35),
            (4, 'Alice Brown', 28)
        ]
        self.db.create_table(self.columns)
        self.db.insert_many_rows(rows)
        # Assert that the rows are inserted successfully
        self.assertCountEqual(rows, self.db.select_all_data())

if __name__ == '__main__':
    unittest.main()