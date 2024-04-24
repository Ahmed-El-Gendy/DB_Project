import pymysql

def update_menu(id ,price, name):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Ramy@123',
        database='hotel',
    )
    try:
        cursor = connection.cursor()
        sql = "UPDATE menu SET price = %s, name = %s WHERE id = %s"
        data = (price, name, id)
        cursor.execute(sql, data)
        connection.commit()
    finally:
        cursor.close()
        connection.close()
if __name__ == "__main__":
    update_menu(4, 30, 'juice')
