#!/usr/bin/python3.7
from smtplib import SMTP
smtpconn = SMTP('10.171.1.129')
#smtpconn = SMTP_PORT(25)
smtpconn.putcmd("vrfy", "msfadmin")
reply = smtpconn.getreply()
smtpconn.quit()

print(reply)
