#!/usr/bin/python3.7

from imaplib import IMAP4_SSL
imapconn = IMAP4_SSL("10.171.1.129")
connection = imapconn.login("msfadmin","msfadmin")
print(connection)


