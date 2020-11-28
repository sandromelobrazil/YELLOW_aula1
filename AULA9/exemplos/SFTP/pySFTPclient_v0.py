#!/usr/bin/python3.7
from pyftpclient.sftp_client import SFTPClient

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


with SFTPClient(**connection_config) as sftpcliconn:
    print(sftpcliconn.listdir('/'))
    sftpcliconn.disconnect
    

