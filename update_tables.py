from datetime import datetime
import pymysql

def insert_tables(table_num, state, guest_id, start, receptionist_id):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Ramy@123',
        database='hotel',
    )
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if state == "Available":
        date = None
    try:
        cursor = connection.cursor()
        sql = "UPDATE tables SET state = %s, guest_id = %s, date = %s, start = %s, receptionist_id = %s WHERE table_num = %s"
        data = (state, guest_id, date, start, receptionist_id, table_num)
        cursor.execute(sql, data)
        connection.commit()
    finally:
        cursor.close()
        connection.close()
if __name__ == "__main__":
    insert_tables(2, "Available", None, None, None)