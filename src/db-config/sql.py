import mysql.connector as mysql
from .credentials import host, user, password


def get_mysql_connection():
    try:
        mysql_db = mysql.connect(host=host, user=user, passwd=password)
        print(f"Connection to the {host} for user {user} created successfully.")
        return mysql_db
    except Exception as ex:
        print(f"Connection could not be made due to the following error: {ex}")
