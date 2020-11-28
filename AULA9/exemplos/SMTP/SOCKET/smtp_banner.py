#!/usr/bin/python3.7
import socket
target = '10.171.1.129'
port = 25 
ok  = '\033[92m[+]\033[0m'

smtpconn=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connect=smtpconn.connect((target,port))
smtpbanner=smtpconn.recv(1024)
print( ok + " - Banner " + str(smtpbanner))
