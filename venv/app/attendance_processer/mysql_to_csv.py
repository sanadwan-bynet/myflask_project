
import pandas as pd
from app.attendance_processer.mysql_connector import (mysql_connect,
                                                      mysql_disconnect)
from app.attendance_processer.sql_queries import select_query

dirpath = 'attendance_csv_files\exported_csv.csv'
def mysql_to_csv():
    conn = mysql_connect()
    cursor = conn.cursor()
    
    sql_query = pd.read_sql_query(select_query, conn)
    df = pd.DataFrame(sql_query)
    df = df.rename(columns={'meeting_name':'Meeting Name', 'meeting_start_time':'Meeting Start Time',
                            'meeting_end_time':'Meeting End Time', 'name':'Name', 'attendee_email':'Attendee Email',
                            'join_time':'Join Time','leave_time':'Leave Time', 'attendance_duration':'Attendance Duration',
                            'connection_type': 'Connection Type'})
    df = df.drop('id', axis=1)
    df.to_csv (dirpath, encoding='utf-16', sep='\t')
    # print(df)
    # cursor.execute(select_query)
    
    # field_names = [i[0] for i in cursor.description]
    # print(field_names)
    # data = cursor.fetchall()
    # print(data)
    # for i,row in empdata.iterrows():
    mysql_disconnect(conn, cursor)
    return dirpath

if __name__ == '__main__':
    mysql_to_csv()
