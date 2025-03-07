import sqlite3

connection = sqlite3.connect("initiate_db.db")
cursor = connection.cursor()
# Создаем таблицу
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
age INTEGER  NOT NULL,
balance INTEGER NOT NULL DEFAULT 1000
)
            ''')
connection.commit()

def is_included(username):
    result = cursor.execute("SELECT * FROM Users WHERE username = ?", (username,)).fetchall()
    connection.commit()
    if result:
        return True
    else:
        return False





# Функция для добавление пользователя
def add_user(username, email, age):
    # Выполняем запрос для вставки.
    cursor.execute("INSERT INTO Users(username,email,age,balance) VALUES(?,?,?,?)", (username, email, age, 1000))
    connection.commit()


# # Проверяем есть ли пользователь с аналогичным именем в БД
# #
# # Добавляем Продукты.
# for i in range(1, 5):
#     cursor.execute("INSERT INTO Products(title,description,price) VALUES(?,?,?)",
#                    (f"Продукт {i}", f"Описание {i}", f"Цена {i * 100}"))
#     connection.commit()
#
#
# def get_all_products():
#     cursor.execute("SELECT * FROM Products")
#     return cursor.fetchall()

