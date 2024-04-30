import pymysql

def show_rooms():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Ramy@123',
        database='hotel',
    )
    try:
        cursor = connection.cursor()
        sql = "SELECT id, class, price_per_night FROM room WHERE state = %s"
        cursor.execute(sql, ("not Occupied",))
        results = cursor.fetchall()
    finally:
        cursor.close()
        connection.close()

        return results
if __name__ == "__main__":
    show_rooms()