import pymysql

def insert_guest_num(guest_id, phone_number):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='***',
        database='hotel',
    )

    try:
        cursor = connection.cursor()
        sql = "INSERT INTO guest_num (guest_id, phone_number) VALUES (%s, %s)"
        data = (guest_id, phone_number)
        cursor.execute(sql, data)
        connection.commit()
    finally:
        cursor.close()
        connection.close()
if __name__ == "__main__":
    insert_guest_num(1,"0120681549")

