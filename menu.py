import pymysql

def insert_menu(id, price, name):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Ramy@123',
        database='hotel',
    )
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO menu (id, price, name) VALUES (%s, %s, %s)"
        data = (id, price, name)
        cursor.execute(sql, data)
        connection.commit()
    finally:
        cursor.close()
        connection.close()
if __name__ == "__main__":
    insert_menu(4, 50, 'juice')