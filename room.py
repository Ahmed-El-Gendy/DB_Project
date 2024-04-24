import pymysql

def insert_room(id, state, clas, price_per_night):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Ramy@123',
        database='hotel',
    )
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO guest (id, state, clas, price_per_night) VALUES (%s, %s, %s, %s)"
        data = (id, state, clas, price_per_night)
        cursor.execute(sql, data)
        connection.commit()
    finally:
        cursor.close()
        connection.close()