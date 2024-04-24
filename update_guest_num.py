import pymysql

def insert_guest_num(guest_id, old_phone_number, new_phone_number):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Ramy@123',
        database='hotel',
    )

    try:
        cursor = connection.cursor()
        sql = "UPDATE guest_num SET phone_number = %s WHERE guest_id = %s and phone_number = %s"
        data = (new_phone_number, guest_id, old_phone_number)
        cursor.execute(sql, data)
        connection.commit()
    finally:
        cursor.close()
        connection.close()
if __name__ == "__main__":
    insert_guest_num(1,"01280348153", '0120681549')

