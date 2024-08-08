import pymysql

# Establish a database connection
connection = pymysql.connect(
    host='localhost',
    user='root',
    password='Ramy@123',
    database='hotel'
)

try:
    with connection.cursor() as cursor:
        # Execute a query
        sql = "SELECT * FROM your_table"
        cursor.execute(sql)
        
        # Fetch all the rows
        result = cursor.fetchall()
        for row in result:
            print(row)
finally:
    # Close the connection
    connection.close()
