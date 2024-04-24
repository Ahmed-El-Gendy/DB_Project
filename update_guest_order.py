import pymysql

def update_guest_order(guest_id, meal_id, number_of_order):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Ramy@123',
        database='hotel',
    )

    try:
        cursor = connection.cursor()
        sql = "UPDATE guest_orders SET number_of_order = %s WHERE guest_id = %s and meal_id = %s"
        data = (number_of_order, guest_id, meal_id)
        cursor.execute(sql, data)
        connection.commit()
    finally:
        cursor.close()
        connection.close()
if __name__ == "__main__":
    update_guest_order(1, 1, 5)

