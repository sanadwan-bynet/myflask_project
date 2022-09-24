import os

import MySQLdb
from dotenv import load_dotenv


load_dotenv()
database_username = os.environ.get('DATABASE_USERNAME')
database_password = os.environ.get('DATABASE_PASSWORD')
database_name = os.environ.get('DATABASE_NAME')
host = os.environ.get('HOST')


def mysql_connect():

    """Connect to a MySQL server using the SSH tunnel connection
    :return connection: Global MySQL database connection
    """

    
    try:
        conn = MySQLdb.connect(
            host = host,
            user = database_username,
            password = database_password,
            database = database_name,
        )
        if not conn.open:
            print('closed')
        print("Connection succeed")
        cursor = conn.cursor()
        cursor.execute("use " + database_name)  
        print("Connected to database " + database_name)
        return conn
    except MySQLdb.Error as e:
        print("Error while connecting to MySQL", e)
  

def mysql_disconnect(conn, cursor):

    """Closes the MySQL database connection.
    """
    cursor.close()
    conn.close()
    print("Disconnected from database " + database_name)

