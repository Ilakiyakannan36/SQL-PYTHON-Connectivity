import mysql.connector
def get_connection():
    try:
        conn=mysql.connector.connect(
            host="localhost",
            port=3306,
            user="root",
            password="ilaki.kannan@04",
            database="ilakiya"
        )
        return conn
    except mysql.connector.Error as e:
        print("Couldn't connect ot Mysql.Please")
        print("Error: ", e)
        return None
        
