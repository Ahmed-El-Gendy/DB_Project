import pymysql

def insert_employee(id, age, nationality, jop, salary, manger_id, name):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Ramy@123',
        database='hotel',
    )

    try:
        cursor = connection.cursor()
        sql = "INSERT INTO employee (id, age, nationality, jop, salary, manger_id, name) VALUES (%s, %s, %s, %s, %s, %s, %s)"
        data = (id, age, nationality, jop, salary, manger_id, name)
        cursor.execute(sql, data)
        connection.commit()
    except pymysql.Error as e:
        print(f"erorr {e}")
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    insert_employee(4, 21, 'egypt', 'receptionist', 5000, 1, 'abass')