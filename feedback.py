import pymysql

def insert_feedback(opinion, rate, guest_id):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Ramy@123',
        database='hotel',
    )
    rate = int(rate)
    guest_id = int(guest_id)
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO feedback (opinion, rate, guest_id) VALUES (%s, %s, %s)"
        data = (opinion, rate, guest_id)
        cursor.execute(sql, data)
        connection.commit()
    finally:
        cursor.close()
        connection.close()
