#!/usr/bin/python3.7
import socket

remoteip = "10.171.1.129"
port=int("110") 

user1='msfadmin' 
pass1='msfadminx' 

#Connect 
pop3conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
pop3conn.connect((remoteip,port))
response1 = pop3conn.recv(2048)

pop3user=('USER ' + user1) 
pop3conn.send(pop3user.encode('ascii') + b'\n')
response2= pop3conn.recv(1024)

pop3pass=('PASS ' + pass1)
pop3conn.send(pop3pass.encode('ascii') +  b'\n')
response3 = pop3conn.recv(2048)

pop3cmd='list'
pop3conn.send(pop3cmd.encode('ascii') +  b'\n')
response4 = pop3conn.recv(2048)


if "+OK" in str(response3):
    print("[+] BINGO - Account: " + user1 + " - Password: " + pass1)
    print(response1)
    print(response2)
    print(response3)
    print(response4)
else:
    print("[-] FAIL - Account: " + user1 + " - Password: " + pass1 )
    print(response1)
    print(response2)
    print(response3)
    print(response4)

pop3conn.close()

