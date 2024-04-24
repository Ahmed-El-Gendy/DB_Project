import pymysql

def update_employee(id, age, nationality, jop, salary, manger_id, name):
    connection = pymysql.connect(
        host='localhost',
        user='root',
        password='Ramy@123',
        database='hotel',
    )

    try:
        cursor = connection.cursor()
        sql = "UPDATE employee set age = %s, nationality = %s, jop = %s, salary = %s, manger_id = %s, name = %s WHERE id = %s"
        data = (age, nationality, jop, salary, manger_id, name, id)
        cursor.execute(sql, data)
        connection.commit()
    except pymysql.Error as e:
        print(f"erorr {e}")
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    update_employee(4, 21, 'egypt', 'receptionist', 5000, 1, 'ahmed abass')