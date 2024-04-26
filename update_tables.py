from datetime import datetime
import pymysql

def update_tables(table_num, guest_id, start, receptionist_id, state):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Ramy@123',
        database='hotel',
    )
    table_num = int(table_num)
    date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    if state == "Available":
        date = None
    try:

        cursor = connection.cursor()
        if state == "Not available":
            sql = "SELECT state FROM tables WHERE table_num = %s"
            cursor.execute(sql, (table_num,))
            results = cursor.fetchall()
            if results[0][0] == 'Not available':
                raise ValueError
        sql = "UPDATE tables SET state = %s, guest_id = %s, date = %s, start = %s, receptionist_id = %s WHERE table_num = %s"
        data = (state, guest_id, date, start, receptionist_id, table_num)
        cursor.execute(sql, data)
        connection.commit()
    finally:
        cursor.close()
        connection.close()
if __name__ == "__main__":
    update_tables(5, 1, "2024-7-21 00:00:00", 2, "Not available")