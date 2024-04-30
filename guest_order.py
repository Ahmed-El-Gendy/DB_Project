import pymysql

def insert_guest_order(guest_id, meal_id, number_of_order):
    if isinstance(meal_id, str):
        sum = 0
        for i in range(4,7):
            if meal_id[i] != ' ':
                sum *= 10
                sum += int(meal_id[i])
        meal_id = sum

    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Ramy@123',
        database='hotel',
    )

    try:
        cursor = connection.cursor()
        sql = "INSERT INTO guest_orders (guest_id, meal_id, number_of_order) VALUES (%s, %s, %s)"
        data = (guest_id, meal_id, number_of_order)
        cursor.execute(sql, data)
        connection.commit()
    finally:
        cursor.close()
        connection.close()
if __name__ == "__main__":
    insert_guest_order(1, 1, 2)

