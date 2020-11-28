#!/usr/bin/python3.7
from pyftpclient.ftp_client import FTPClient

target = "10.171.1.129"
username = "msfadmin"
password = "msfadmin"
port = '21'

connection_config = {
    'hostname': target,
    'username': username,
    'password': password,
    'port': int(port)
}


with FTPClient(**connection_config) as ftpcliconn:
    print(ftpcliconn.listdir('/'))
    ftpcliconn.disconnect
    

