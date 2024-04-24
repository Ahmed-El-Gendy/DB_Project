import pymysql

def update_feedback(id, opinion, rate, guest_id):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Ramy@123',
        database='hotel',
    )

    try:
        cursor = connection.cursor()
        sql = "UPDATE feedback SET opinion = %s, rate = %s WHERE id = %s"
        data = (opinion, rate, id)
        cursor.execute(sql, data)
        connection.commit()
    finally:
        cursor.close()
        connection.close()
if __name__ == "__main__":
    update_feedback(1,'well done', 10, 1)
