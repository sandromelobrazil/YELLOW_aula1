#!/usr/bin/python3.7
import telnetlib
target = "10.171.1.129"
username = "msfadmin"
password = "msfadmin"

telnetconn = telnetlib.Telnet(target)

telnetconn.read_until(b"login: ")
telnetconn.write(username.encode('ascii') + b"\n")

if password:
    telnetconn.read_until(b"Password: ")
    telnetconn.write(password.encode('ascii') + b"\n")

telnetconn.write(b"pwd\n")
telnetconn.write(b"ls -l \n")
telnetconn.write(b"exit\n")

print(telnetconn.read_all().decode('ascii'))
