# Flask project

Flask project gets the attendance csv files from the machine as required and puts them into
the Mysql database. uses the attendance python script to parse all the csv files and calculates
the attendance percintage from all the meeting, and dump it into a new csv file that includes a column
for every meeting and the percintage at the last column (Yona's script)

### Installation

```bash
# Install dependencies
pip3 install -r requirements.txt

# Export env variables
DATABASE_PASSWORD=<db_password>
DATABASE_NAME=<db_name>
DATABASE_USERNAME=<db_username>
HOST=<hostname>

CSV_HOST=<csv_hostname>
CSV_USERNAME=<csv_host_username>
CSV_PASSWORD=<csv_password>

# Run the app
flask run
```
### Extension:



### API

```bash
GET http://localhost:5000/
```
### attendance_from_csv.py
first checks if the row exists in the table
insert the rows of an given csv into the MySQL table.

### get_csv_files.py
the script gets the csv file from the remote machine using sftp 

### mysql_connector
connects to MySQL server using the extension MySQLdb
returns the connection object and the cursor

### mysql_to_csv.py
gets the table from MySQL database and dump it into csv file called 'exported_csv.csv'

### parse_attendance
gets the attendace table from MySQL database, parses the data to calculate the percintage of
attendance time and dump the results to a csv file called 'attendance.py'

### sql_queries.py
contains all the sql queries used in the scripts

### webapp.py
the entry point for the flask app

clone the [project](https://github.com/sanadwan-bynet/myflask_project.git).

![image](https://user-images.githubusercontent.com/112401895/193425078-7815f343-eea6-473b-91cb-aef3ca9c9849.png)

/Home
![image](https://user-images.githubusercontent.com/112401895/193425095-8355c34a-57e8-4979-aeaf-76af1eadaea2.png)

/attendance
![image](https://user-images.githubusercontent.com/112401895/193425192-8d9119d1-b45b-4cbd-85b5-54894dc375ab.png)


Images
![image](https://user-images.githubusercontent.com/112401895/193425110-9710eeba-9e20-4fc4-bf5a-d3e06891dbfc.png)

Containers
![image](https://user-images.githubusercontent.com/112401895/193425115-054aba91-5d4b-4b4c-ab82-339f9e2138da.png)

Volumes
![image](https://user-images.githubusercontent.com/112401895/193425141-e2bd7f4f-ed13-481d-a426-81c50e203c66.png)


