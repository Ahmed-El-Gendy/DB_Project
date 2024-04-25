import pymysql

def insert_room(clas, price_per_night, state):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Ramy@123',
        database='hotel',
    )
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO room (state, class, price_per_night) VALUES (%s, %s, %s)"
        data = (state, clas, price_per_night)
        cursor.execute(sql, data)
        connection.commit()
    finally:
        cursor.close()
        connection.close()
if __name__ == "__main__":
    insert_room('Not occupied', 'A', 200)