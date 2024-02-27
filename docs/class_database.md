# My_Database Class

The My_Database class provides a simple interface to interact with a SQLite database. It includes methods for creating tables, inserting data, selecting data, updating data, deleting data, dropping tables, and closing connections.

## Initialization

To use the My_Database class, initialize it with the following parameters:

- `db_name` (str): Name of the SQLite database file.
- `tb` (str): Name of the table in the database.

Example Initialization:

```python
from my_database import My_Database

# Initialize with database name and table name
db = My_Database(db_name='database.db', tb='tourevent')
```

## Methods

- `create_table(columns)`  
   Creates a table in the database with the specified columns.
- `insert_many_rows(rows, columns)`  
   Inserts multiple rows of data into the table.
  Filters out rows that already exist in the table.
- `insert_one_row(row)`
  Inserts a single row of data into the table.
  Skips insertion if the row already exists.
- `select_all_data()`
  Retrieves all data from the table.
- `select_one_data(condition)`
  Retrieves a single row of data based on the specified condition.
- `update_data(condition, new_data)`
  Updates data in the table based on the specified condition and new data.
- `delete_data(condition)`
  Deletes data from the table based on the specified condition.
- `drop_table()`
  Drops (deletes) the entire table from the database.
- `close_connection()`
  Closes the connection to the database.

## Example Usage

```python
# Create table
columns = ['id INTEGER PRIMARY KEY', 'band TEXT', 'city TEXT', 'date TEXT']
db.create_table(columns)

# Insert new rows
new_rows = [
  ('2024-02-25 17:19:59', 'The Rolling Stones', 'The Forum', '1975.07.11'),
  ('2024-02-25 17:20:00', 'The Rolling Stones', 'The Forum', '1975.07.11'),
]
db.insert_many_rows(new_rows)

# Delete data
db.delete_data("city='The Forum'")

# Select all data
data = db.select_all_data()
print(data)

# Close connection
db.close_connection()
```

## Important Notes

- This class provides basic CRUD (Create, Read, Update, Delete) operations for SQLite databases.

- Ensure the required sqlite3 library is installed.

- The script initializes the My_Database class, creates a table, inserts data, deletes data, selects data, and then closes the connection.

- Modify the columns variable to match the schema of your table.

- The script demonstrates basic usage of the My_Database class methods.
