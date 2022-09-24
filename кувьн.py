import sqlite3

connection = sqlite3.connect('NEW_SQL_STAS.db')
cursor = connection.cursor()

def print_groups():
    result = cursor.execute("""
    SELECT students.name, students.age, groups.name 
    FROM students
    JOIN groups ON students.groups.id = groups.id
    """).fetchall()
    print(result)

def add_groups(name, description):
    cursor.execute("""
    INSERT INTO groups (name, description)
    VALUES (?, ?)""", (name, description))
    connection.commit()

def add_students(name, age, group_name):
    group_id = cursor.execute("""
    SELECT id
    FROM groups
    WHERE name = ?""", (group_name,)).fetchall()
    if group_id is None:
        print('Такой группы нет')
        return
    cursor.execute("""
    INSERT INTO groups (name, age, group_id)
    VALUES (?, ?, ?)""", (name, age, group_id[0]))
    connection.commit()
    print('студент добавлен')

def remove_students(name):
    cursor.execute("""
    DELETE FROM students
    WHERE name = ?""", (name,))
    connection.commit()

def remove_group(name):
    cursor.execute("""
    DELETE FROM group
    WHERE name = ?""", (name,))
    connection.commit()

add_students('Васильева Даша', 56, 'Программирование на Python')
print_students()
remove_student('Васильева Даша')
print_students()