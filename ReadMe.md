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

clone the [project](https://github.com/sanadwan-bynet/Flask_project.git).


