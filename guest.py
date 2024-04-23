import pymysql

def insert_guest(id, name, age, nationality):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Ramy@123',
        database='hotel',
    )

    try:
        cursor = connection.cursor()
        sql = "INSERT INTO guest (id, name, age, nationality) VALUES (%s, %s, %s, %s)"
        data = (id, name, age, nationality)
        cursor.execute(sql, data)
        connection.commit()
    finally:
        cursor.close()
        connection.close()