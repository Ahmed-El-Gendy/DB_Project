import pymysql
from datetime import datetime, timedelta

def update_room1(id, state, guest_id = None, receptionist_id = None, interval_duration = None):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Ramy@123',
        database='hotel',
    )
    try:
        if interval_duration != None:
            if state == 'Occupied':
                cursor = connection.cursor()
                sql = "SELECT state FROM room WHERE id = %s"
                cursor.execute(sql, (id,))
                results = cursor.fetchall()
                if results[0][0] == 'Occupied':
                    raise ValueError
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


def update_room(id, guest_id=None, receptionist_id=None, interval_duration=None):
    state = 'Occupied'
    if isinstance(id, str):
        sum = 0
        for i in range(4,7):
            if id[i] != ' ':
                sum *= 10
                sum += int(id[i])
        id = sum
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Ramy@123',
        database='hotel',
    )
    try:
        if interval_duration != None:
            if state == 'Occupied':
                cursor = connection.cursor()
                sql = "SELECT state FROM room WHERE id = %s"
                cursor.execute(sql, (id,))
                results = cursor.fetchall()
                if results[0][0] == 'Occupied':
                    raise ValueError
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

