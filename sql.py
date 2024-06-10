import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(
        host='127.0.0.1',
        user='root',
        password='12345',
        auth_plugin='mysql_native_password'
    )
    if conn.is_connected():
        print('Connection established')
        mycursor = conn.cursor()
except Error as e:
    print(f'Connection error: {e}')
