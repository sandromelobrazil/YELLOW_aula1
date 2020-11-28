#!/usr/bin/python3.7
import socket
from smtplib import SMTP
smtpconn = SMTP('10.171.1.129')
username = "root"

fail = '\033[91m[-]\033[0m'
ok  = '\033[92m[+]\033[0m'
okok  = '\033[92m[*]\033[0m'

msg=smtpconn.helo("oi")
print( okok + " Server " + str(msg))

smtpinfo = smtpconn.help()

if "Error" in str(smtpinfo):
    print(fail + " Help is not available")
else:
    print(ok + " Help is available")


def checksmtpcmd(_cmd):
    smtpconn.putcmd(_cmd, username)
    cmdreply = smtpconn.getreply()
    return cmdreply

if 502 in checksmtpcmd("expn"):
    print(fail + " EXPN command is not available")
else:
    print(ok + " EXPN command is available")
    

if 502 in checksmtpcmd("vrfy"):
    print(fail + " VRFY command is not available")
else:
    print( ok + " VRFY command is available")
    
smtpconn.quit()
