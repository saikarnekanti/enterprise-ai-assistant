import sqlite3
connection=sqlite3.connect("users.db")

cursor=connection.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER NOT NULL,
    is_learning_ai BOOLEAN NOT NULL
)
""")

connection.commit()

cursor.execute("SELECT * FROM users")
rows=cursor.fetchall()
print(rows)

connection.close()



