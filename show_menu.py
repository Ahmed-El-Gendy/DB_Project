import pymysql

def show_menu():
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Ramy@123',
        database='hotel',
    )
    try:
        cursor = connection.cursor()
        sql = "SELECT id, name, price FROM menu"
        cursor.execute(sql)
        results = cursor.fetchall()
    finally:
        cursor.close()
        connection.close()
        return results
if __name__ == "__main__":
    show_menu()