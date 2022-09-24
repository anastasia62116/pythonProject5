import sqlite3

connection = sqlite3.connect('db.bd')
cursor = connection.cursor()

name = 'Иванов Иван'
result = cursor.execute("""SELECT * FROM students
                  WHERE name = ?""", (name,)).fetchall()
print(result)