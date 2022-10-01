from genericpath import isfile
import os

import pysftp
from dotenv import load_dotenv

load_dotenv()

csv_host = os.environ.get('CSV_HOST')
csv_username = os.environ.get('CSV_USERNAME')
csv_password = os.environ.get('CSV_PASSWORD')

cwd = os.getcwd()
dirpath= cwd + '/app/attendance_processer/attendance_csv_files/'
rempath='/var/tmp/csv_files/'
cnopts = pysftp.CnOpts()  
cnopts.hostkeys = None    

"""
    get the csv files from the remote machine and put it into the directory  
    :return: path of the directory where the csv files where copied to
    """
def get_files_from_host():
    with pysftp.Connection(host=csv_host, username=csv_username, password=csv_password, cnopts=cnopts) as sftp:
        print("Connection succesfully stablished ... ")
        print(dirpath)
        print(rempath)
        sftp.cwd(rempath)
        list_dir = sftp.listdir_attr()  # Returns sorted files list. (Sorted by SFTPAttribute.filename.)
        for attribute in list_dir:
            file_name = attribute.filename
            if(not os.path.isfile(dirpath + file_name)):
                remote = rempath + file_name
                local = dirpath + file_name 
                sftp.get(remote, local)         # get a remote file
                
    return dirpath


def get_files(dirpath):
    """
    calculates a list containing all participants files
    :param dirpath: string of a directory containing the participants files
    :return: list of all participants files
    """
    attend_files = []
    for file in os.listdir(dirpath):
        filepath = os.path.join(dirpath, file)
        if os.path.isfile(filepath) and "participant-" in file:
            attend_files.append(filepath)

    if len(attend_files) == 0:
        print("This directory has no participant's meetings files!")
        print("please provide a one containing those csv files")
        exit(1)
    return attend_files
