import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("PRAGMA table_info(clients)")
columns = cursor.fetchall()

for column in columns:
    print(column)

conn.close()
