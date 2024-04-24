import pymysql

def insert_bill(guest_id, receptionist_id):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Ramy@123',
        database='hotel',
    )

    try:

        total = 0
        cursor = connection.cursor()
        sql = "SELECT price_per_night FROM room WHERE guest_id = %s"
        cursor.execute(sql, (guest_id,))
        results = cursor.fetchall()
        total += int(results[0][0])
        sql = "INSERT INTO bill (total_price, guest_id, date_of_check_out, receptionist_id) VALUES (%s, %s, NOW(), %s)"
        data = (total, guest_id, receptionist_id)
        cursor.execute(sql, data)
        connection.commit()
    except pymysql.Error as e:
        print(f"erorr {e}")
    finally:
        cursor.close()
        connection.close()
if __name__ == "__main__":
    insert_bill(1, 2)