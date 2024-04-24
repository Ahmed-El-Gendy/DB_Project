import pymysql

def update_guest(id, name, age, nationality):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Ramy@123',
        database='hotel',
    )

    try:
        cursor = connection.cursor()
        sql = "UPDATE guest SET name = %s, age = %s, nationality = %s WHERE id = %s"
        data = (name, age, nationality, id)
        cursor.execute(sql, data)
        connection.commit()
    finally:
        cursor.close()
        connection.close()
if __name__ == "__main__":
    update_guest(45, 'ahmed', 21, 'egypt')