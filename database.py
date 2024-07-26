import sqlite3

def create_table():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('''
    CREATE TABLE person (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        last_name TEXT,
        age INTEGER,
        email TEXT
    )
    ''')
    conn.commit()
    conn.close()

def rename_table():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('ALTER TABLE person RENAME TO employee')
    conn.commit()
    conn.close()

def remove_column():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    c.execute('CREATE TABLE new_employee (id INTEGER PRIMARY KEY, first_name TEXT, last_name TEXT, age INTEGER)')
    c.execute('INSERT INTO new_employee (id, first_name, last_name, age) SELECT id, first_name, last_name, age FROM employee')
    c.execute('DROP TABLE employee')
    c.execute('ALTER TABLE new_employee RENAME TO employee')
    conn.commit()
    conn.close()

def insert_data():
    conn = sqlite3.connect('example.db')
    c = conn.cursor()
    employees = [
        (1, 'Анна', 'Иванова', 28),
        (2, 'Борис', 'Петров', 34),
        (3, 'Вера', 'Сидорова', 24),
        (4, 'Глеб', 'Михайлов', 46),
        (5, 'Дарья', 'Кузнецова', 32),
        (6, 'Егор', 'Федоров', 29)
    ]
    c.executemany('INSERT INTO employee (id, first_name, last_name, age) VALUES (?, ?, ?, ?)', employees)
    conn.commit()
    conn.close()

if __name__ == '__main__':
    create_table()
    rename_table()
    remove_column()
    insert_data()
