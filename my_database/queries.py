import sqlite3

def get_data():
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    cursor.execute("""
        SELECT 
            c.full_name,
            co.number,
            co.date,
            co.status AS contract_status,
            s.name AS stage_name,
            s.start_date,
            s.end_date,
            s.status AS stage_status
        FROM 
            clients c
        JOIN 
            contracts co ON c.id = co.client_id
        JOIN 
            stages s ON co.id = s.contract_id
    """)

    rows = cursor.fetchall()

    conn.close()

    return rows

if __name__ == '__main__':
    data = get_data()
    for row in data:
        print(row)
