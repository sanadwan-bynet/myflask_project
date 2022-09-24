import datetime
import logging

from calendar import c
from locale import currency
import MySQLdb
import pandas as pd


from app.attendance_processer.sql_queries import *


# database_username = 'root'
# database_password = os.environ.get('Sa20770Ad!')
# database_name = 'sanad_1'
# localhost = '127.0.0.1'

"""
    check if an given row exists in the given table
    :param row: the row we want to check
    :param cursor: the MySQL connection cursor
    :return: if the row exists, return true else return false
    """
def check_row(row, cursor):
    # if an Email doesn't exist we skip it
    if "nan" in str(row['Attendee Email']):
        print("skipped")
        return True
    cursor.execute(select_row, tuple(row))
    
    if cursor.rowcount > 0:
        print("record exists in table")
        # print(tuple(row))
        return True
    return False
    
"""
    inserts the csv files into the table after establishing a MySQL connection
    building a dataframe from the given files,
    check if there is already a table in the database, if there isn't 
    creating MySQL table and insert each row from the dataframe into the table
    """
def insert_to_db(filename, conn, cursor):

    # filename = sys.argv[1]
    
    # read the csv file
    empdata = pd.read_csv(filename, encoding='utf-16', engine='python', sep='\t')
    
    # connect to MySQL server and get an instance of a cursor
    

    try:
        
        # check if there is already a table in the database
        cursor.execute("SHOW TABLES LIKE 'attendance'")
        results = cursor.fetchall()
        # print(results)

        # create a new table in the database only if it doesn't exists
        if not results:
            cursor.execute(create_table)
            print("execute succeed")

        
        # adjust the timestamp in the dataframe to fit into the table            
        empdata['Attendance Duration'] = empdata['Attendance Duration'].str.split(' ').str[0].astype(int)
        empdata["Meeting Start Time"] = datetime.datetime.strptime(empdata["Meeting Start Time"][0][1:], '"%Y-%m-%d %H:%M:%S"')
        empdata["Meeting End Time"] = datetime.datetime.strptime(empdata["Meeting End Time"][0][1:], '"%Y-%m-%d %H:%M:%S"')
        empdata["Join Time"] = datetime.datetime.strptime(empdata["Join Time"][0][1:], '"%Y-%m-%d %H:%M:%S"')
        empdata["Leave Time"] = datetime.datetime.strptime(empdata["Leave Time"][0][1:], '"%Y-%m-%d %H:%M:%S"')
        # loop over the rows in the dataframe and insert each one into the table
        for i,row in empdata.iterrows():
            #here %S means string values 
            exists = check_row(row, cursor)
            if exists:
                continue
            if "nan" in str(row['Attendee Email']):
                continue
            # print(tuple(row))
            # excute the MySQL query that inserts the row into the table
            cursor.execute(insert_row, tuple(row))
            conn.commit()
            # print(i, " Record inserted")
         
        # disconnect from MySQL server    
        
    except MySQLdb.Error as e:
        print("Error while connecting to MySQL", e)
    
    


