import psycopg2
from psycopg2 import sql

conn = psycopg2.connect(
    dbname="",
    user="",
    password="",
    host="",
    port=1234
)

cur = conn.cursor()

def read_all_rows():
    cur.execute("SELECT * FROM your_table")
    rows = cur.fetchall()
    return rows

def read_one_row(primary_key):
    cur.execute("SELECT * FROM your_table WHERE id = %s", (primary_key,))
    row = cur.fetchone()
    return row

def create_row(data):
    query = sql.SQL("INSERT INTO your_table (column1, column2, column3) VALUES (%s, %s, %s)")
    cur.execute(query, (data['value1'], data['value2'], data['value3']))
    conn.commit()

def delete_row(primary_key):
    cur.execute("DELETE FROM your_table WHERE id = %s", (primary_key,))
    conn.commit()

all_rows = read_all_rows()
print("All rows:", all_rows)

one_row = read_one_row(1)
print("One row:", one_row)

new_data = {'value1': 'example_value1', 'value2': 'example_value2', 'value3': 'example_value3'}
create_row(new_data)

delete_row(1)

cur.close()
conn.close()
