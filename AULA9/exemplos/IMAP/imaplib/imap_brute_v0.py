#!/usr/bin/python3.7

from imaplib import IMAP4
imapconn = IMAP4("10.171.1.129")
connection = imapconn.login("msfadmin","msfadmin")
print(connection)


