import sqlite3


def process_payment(payment_data):
    """Обрабатывает поступление платежа."""
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    for payment in payment_data:
        # Проверка суммы платежа
        if payment['amount'] <= 0:
            continue  # Пропускаем некорректные платежи

        # Обновление баланса клиента
        client = get_client(payment['client_id'], cursor)
        if client:
            client_id, client_name, client_balance = client
            new_balance = client_balance + payment['amount']
            update_client_balance(payment['client_id'], new_balance, cursor)

            # Создание записи о платеже
            create_payment_record(payment, cursor)

            # Обновление статуса договора, если необходимо
            update_contract_status(payment['contract_id'], cursor)

    conn.commit()
    conn.close()


def get_client(client_id, cursor):
    """Получение данных клиента из базы данных."""
    cursor.execute("SELECT id, full_name, balance FROM clients WHERE id = ?", (client_id,))
    return cursor.fetchone()


def update_client_balance(client_id, new_balance, cursor):
    """Обновление баланса клиента в базе данных."""
    cursor.execute("UPDATE clients SET balance = ? WHERE id = ?", (new_balance, client_id))


def create_payment_record(payment, cursor):
    """Создание записи о платеже в базе данных."""
    cursor.execute("""
        INSERT INTO payments (client_id, contract_id, amount, payment_date)
        VALUES (?, ?, ?, ?)
    """, (payment['client_id'], payment['contract_id'], payment['amount'], payment['payment_date']))


def update_contract_status(contract_id, cursor):
    """Обновление статуса договора в базе данных."""
    # Здесь должна быть логика обновления статуса договора в зависимости от условий
    pass


if __name__ == '__main__':
    # Пример использования:
    payment_data = [
        {'client_id': 1, 'contract_id': 101, 'amount': 100, 'payment_date': '2024-01-28'},
        {'client_id': 2, 'contract_id': 102, 'amount': 200, 'payment_date': '2024-01-28'}
    ]
    process_payment(payment_data)
