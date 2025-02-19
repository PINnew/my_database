import sqlite3


def create_database():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Создание таблицы клиентов
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY,
            full_name TEXT NOT NULL
        )
    """)

    # Создание таблицы контрактов
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contracts (
            id INTEGER PRIMARY KEY,
            client_id INTEGER,
            number TEXT NOT NULL,
            date DATE NOT NULL,
            status TEXT NOT NULL,
            FOREIGN KEY (client_id) REFERENCES clients(id)
        )
    """)

    # Создание таблицы платежей
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY,
            client_id INTEGER,
            contract_id INTEGER,
            amount REAL NOT NULL,
            payment_date DATE NOT NULL,
            FOREIGN KEY (client_id) REFERENCES clients(id),
            FOREIGN KEY (contract_id) REFERENCES contracts(id)
        )
    """)

    # Добавляем колонку balance
    cursor.execute("ALTER TABLE clients ADD COLUMN balance REAL DEFAULT 0")

    conn.commit()
    conn.close()

# Вызов функции для создания базы данных и таблиц
if __name__ == '__main__':
    create_database()
