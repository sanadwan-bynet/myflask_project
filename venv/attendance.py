import datetime
import pandas as pd
import os, sys


def csv_fun():

    if len(sys.argv) != 2:
        print("Usage: md5sum.py <dir>")
        sys.exit(2)
    dic = sys.argv[1]
    combine_csv = pd.DataFrame(columns=['Name', 'Duration'])

    count_time = 0

    for f in os.listdir(dic):
        file = os.path.join(dic, f)

        if os.path.isfile(file) and str(file).endswith(".csv"):
            data = pd.read_csv(file, encoding='utf-16', engine='python', sep='\t')

            start_time = datetime.datetime.strptime(data["Meeting Start Time"][0][1:], '"%Y-%m-%d %H:%M:%S"')
            end_time = datetime.datetime.strptime(data["Meeting End Time"][0][1:], '"%Y-%m-%d %H:%M:%S"')
            count_time += ((end_time - start_time).total_seconds() / 60)

            data["Meeting Start Time"] = datetime.datetime.strptime(data["Meeting Start Time"][0][1:], '"%Y-%m-%d %H:%M:%S"')
            data["Meeting End Time"] = datetime.datetime.strptime(data["Meeting End Time"][0][1:], '"%Y-%m-%d %H:%M:%S"')

            data['Duration'] = data['Attendance Duration'].str.split(' ').str[0]
            data['Duration'] = data['Duration'].astype(int)
            name_df = data.groupby('Name').sum()


            combine_csv = pd.merge(combine_csv, name_df, on="Name", how="outer")
            combine_csv = combine_csv.fillna(0)
            combine_csv["Duration"] = combine_csv["Duration_x"] + combine_csv["Duration_y"]
            combine_csv.drop(['Duration_x', 'Duration_y'], axis=1, inplace=True)

    combine_csv["Total Attendance Time in percent"] = (combine_csv["Duration"] / count_time).round(2) * 100
    combine_csv.rename(columns={"Duration": "Total time "}, inplace=True)
    combine_csv.to_csv('total_attendance.csv')



