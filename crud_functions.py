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
    create_table_query = f'''
    CREATE TABLE IF NOT EXISTS Products(
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        description TEXT,
        price INTEGER NOT NULL
    )
    '''
    execute_query(create_table_query)


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
