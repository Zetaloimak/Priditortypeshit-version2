import sqlite3

conn = sqlite3.connect('priditor.db')
cursor = conn.cursor()
cursor.execute('''CREATE TABLE IF NOT EXISTS USERS
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                password TEXT NOT NULL)
                ''')
conn.commit()
 
def user():
    username = input("please input your username :")
    password = input("please input your password :")
    cursor.execute("INSERT INTO USERS (username, password) VALUES (?, ?)", (username, password))
    conn.commit()