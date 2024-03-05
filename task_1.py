"""homework~"""

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

def update_row(primary_key, new_data):
    query = sql.SQL("UPDATE your_table SET column1 = %s, column2 = %s, column3 = %s WHERE id = %s")
    cur.execute(query, (new_data['value1'], new_data['value2'], new_data['value3'], primary_key))
    conn.commit()

def delete_row(primary_key):
    cur.execute("DELETE FROM your_table WHERE id = %s", (primary_key,))
    conn.commit()

cur.close()
conn.close()
