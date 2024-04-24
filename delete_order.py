import pymysql


def delete_orders(guest_id):
    connection = pymysql.connect(host='localhost',user='root',
                                password='Ramy@123',
                                database='hotel')

    try:
        cursor = connection.cursor()
        delete_query = "DELETE FROM guest_orders WHERE guest_id = %s"
        cursor.execute(delete_query, (guest_id,))
        connection.commit()
    except pymysql.Error as e:
        print(e)
    finally:
        cursor.close()
        connection.close()
if __name__ == "__main__":
    delete_orders(1)