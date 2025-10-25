import mysql.connector
conn=mysql.connector.connect (
    host="localhost",
    port=3306,
    user="root",
    password="ilaki.kannan@04",
    database="ilakiya"
)
if conn.is_connected():
    print("Connection Successful")
else:
    print("Connection Failed")
    