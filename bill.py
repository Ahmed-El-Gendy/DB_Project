import pymysql
from update_room import update_room1
from delete_order import delete_orders
def insert_bill(guest_id, receptionist_id):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Ramy@123',
        database='hotel',
    )

    try:
        check = []
        total = 0
        cursor = connection.cursor()
        sql = "SELECT name FROM guest WHERE id = %s"
        cursor.execute(sql, (guest_id,))
        results = cursor.fetchall()
        check.append(str(f"{results[0][0]}"))
        sql = "SELECT price_per_night, interval_duration FROM room WHERE guest_id = %s"
        cursor.execute(sql, (guest_id,))
        results = cursor.fetchall()
        total += int(results[0][0] * results[0][1])
        check.append(str(f"Price per night: {results[0][0]}\nNum of days: {results[0][1]}\n"))

        sql = "SELECT menu.price, guest_orders.number_of_order, menu.name FROM guest_orders join menu on guest_orders.guest_id = %s and guest_orders.meal_id = menu.id"
        cursor.execute(sql, (guest_id,))
        results = cursor.fetchall()
        for rwo in results:
            total += int(rwo[0]) * int(rwo[1])
            check.append(str(f"name: {rwo[2]} price: {rwo[0]} count: {rwo[1]}"))
        check.append(str(f"{total}"))
        sql = "INSERT INTO bill (total_price, guest_id, date_of_check_out, receptionist_id) VALUES (%s, %s, NOW(), %s)"
        data = (total, guest_id, receptionist_id)
        cursor.execute(sql, data)
        connection.commit()
        sql = "SELECT id FROM room WHERE guest_id = %s"
        cursor.execute(sql, (guest_id,))
        results = cursor.fetchall()
        update_room1(int(results[0][0]), 'Not occupied', None, None, None)
        delete_orders(guest_id)
    except pymysql.Error as e:
        print(f"erorr {e}")
    finally:
        cursor.close()
        connection.close()
        return check
if __name__ == "__main__":
    insert_bill(1, 2)