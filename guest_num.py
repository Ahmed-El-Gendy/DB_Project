import pymysql

def insert_guest_num(guest_id, phone_number):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Ramy@123',
        database='hotel',
    )

    try:
        cursor = connection.cursor()
        sql = "INSERT INTO guest (guest_id, phone_number) VALUES (%s, %s)"
        data = (guest_id, phone_number)
        cursor.execute(sql, data)
        connection.commit()
    finally:
        cursor.close()
        connection.close()