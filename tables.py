from datetime import datetime
import pymysql

def insert_tables(table_num, state, chairs_num, guest_id, start, receptionist_id):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Ramy@123',
        database='hotel',
    )
    date = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO guest (table_num, state, chairs_num, guest_id, date, start, receptionist_id) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (table_num, state, chairs_num, guest_id, date, start, receptionist_id)
        cursor.execute(sql, data)
        connection.commit()
    finally:
        cursor.close()
        connection.close()