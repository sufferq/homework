import sqlite3

connection = sqlite3.connect('products.db')
cursor = connection.cursor()


def initiate_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Users(
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL
        )
    ''')
    connection.commit()

def get_all_products():
    cursor.execute('SELECT * FROM Products')
    return cursor.fetchall()


def add_user(username, email, age, balance=1000):
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)',(username, email, age, balance))
    connection.commit()


def is_included(username):
    connection = sqlite3.connect("products.db")
    cursor = connection.cursor()
    check_user = cursor.execute("SELECT * FROM Users WHERE username =? ", (username,))
    if check_user.fetchone() is None:
        connection.commit()
        connection.close()
        return False
    else:
        connection.commit()
        connection.close()
        return True


if __name__ == '__main__':
    initiate_db()