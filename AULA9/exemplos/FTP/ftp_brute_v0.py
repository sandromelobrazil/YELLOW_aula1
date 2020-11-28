#!/usr/bin/python3.7

from ftplib import FTP
ftpconn = FTP("10.171.1.129")
connection = ftpconn.login("msfadmin","msfadmin")
print(connection)


