import sqlite3

def populate_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Добавление клиентов
    cursor.execute("INSERT INTO clients (full_name, balance) VALUES (?, ?)", ('Иванов Иван', 1000))
    cursor.execute("INSERT INTO clients (full_name, balance) VALUES (?, ?)", ('Петров Петр', 1500))

    # Добавление контрактов
    cursor.execute("INSERT INTO contracts (client_id, number, date, status) VALUES (?, ?, ?, ?)", (1, 'C001', '2025-01-01', 'Активен'))
    cursor.execute("INSERT INTO contracts (client_id, number, date, status) VALUES (?, ?, ?, ?)", (2, 'C002', '2025-01-02', 'Активен'))

    conn.commit()
    conn.close()

if __name__ == '__main__':
    populate_data()
