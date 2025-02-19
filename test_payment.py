from services.payment_service import process_payment

def test_process_payment():
    payment_data = [
        {'client_id': 1, 'contract_id': 1, 'amount': 200, 'payment_date': '2025-01-28'},
        {'client_id': 2, 'contract_id': 2, 'amount': 300, 'payment_date': '2025-01-28'},
        {'client_id': 1, 'contract_id': 1, 'amount': -50, 'payment_date': '2025-01-28'},  # Некорректный платеж
    ]

    process_payment(payment_data)

if __name__ == '__main__':
    test_process_payment()
