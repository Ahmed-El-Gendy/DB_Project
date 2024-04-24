from datetime import datetime
import pymysql

def insert_tables(table_num, state, chairs_num):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Ramy@123',
        database='hotel',
    )
    try:
        cursor = connection.cursor()
        sql = "INSERT INTO tables (table_num, state, chairs_num) VALUES (%s, %s, %s)"
        data = (table_num, state, chairs_num)
        cursor.execute(sql, data)
        connection.commit()
    finally:
        cursor.close()
        connection.close()
if __name__ == "__main__":
    insert_tables(30, "Available", 5)