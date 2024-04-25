import pymysql
from datetime import datetime, timedelta

def update_room(id, state, guest_id = None, receptionist_id = None, interval_duration = None):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Ramy@123',
        database='hotel',
    )
    print(f"{id} {guest_id} {receptionist_id} {interval_duration} {state}")
    try:
        if interval_duration != None:
            id = int(id)
            interval_duration = int(interval_duration)
            receptionist_id = int(receptionist_id)
            date = datetime.now().strftime("%Y-%m-%d")
            end_date = (datetime.now() + timedelta(days=interval_duration)).strftime("%Y-%m-%d")
        else:
            date = None
            end_date = None
        cursor = connection.cursor()
        sql = "UPDATE room SET state = %s, guest_id = %s, receptionist_id = %s, interval_duration = %s, start_date = %s, end_date = %s WHERE id = %s"
        data = (state, guest_id, receptionist_id, interval_duration, date, end_date , id)
        cursor.execute(sql, data)
        connection.commit()
    finally:
        cursor.close()
        connection.close()
if __name__ == "__main__":
    update_room(1,None,None,None,'Not occupied')
