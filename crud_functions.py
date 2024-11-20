import sqlite3


# Функция для создания подключения и выполнения SQL-запросов
def execute_query(query, params=(), fetch=False):
    with sqlite3.connect('telegram.db') as connection:
        cursor = connection.cursor()
        cursor.execute(query, params)
        if fetch:
            return cursor.fetchall()
        connection.commit()


def initiate_db():
    # Создание таблицы, если она не существует
    create_table_query_1 = f'''
        CREATE TABLE IF NOT EXISTS Products(
            id INTEGER PRIMARY KEY,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
        '''
    create_table_query_2 = f'''
        CREATE TABLE IF NOT EXISTS Users(
            id INTEGER PRIMARY KEY,
            username TEXT NOT NULL,
            email TEXT NOT NULL,
            age INTEGER NOT NULL,
            balance INTEGER NOT NULL
        )
        '''
    execute_query(create_table_query_1)
    execute_query(create_table_query_2)


# Добавление записей в таблицу
# for i in range(1, 5):
#     execute_query(
#         "INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
#         (f'Продукт {i}', f'Описание {i}', 100 * i)
#     )

def get_all_products():
    select_query = "SELECT * FROM Products"
    products = execute_query(select_query, fetch=True)
    return products


def add_user(username: str, email: str, age: int, balance: int = 1000):
    execute_query(
             "INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
             (username, email,age,balance)
         )

def is_included(username: str):
    select_query = "SELECT 1 FROM Users WHERE username = ? LIMIT 1"
    if execute_query(select_query, (username,), fetch=True):
        return True
    else:
        return False

