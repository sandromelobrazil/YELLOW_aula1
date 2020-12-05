#!/usr/bin/python

from ftplib import FTP

target = '11.11.11.171'
user = 'msfadmin'
pwd  = 'msfadmin'

ftpconn = FTP(target)

connection = ftpconn.login(user,pwd)

print(connection)


