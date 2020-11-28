#!/usr/bin/python3.7
import poplib

username='msfadmin'
password='msfadmin'

pop3conn =  poplib.POP3_SSL('10.171.1.129', '995')
pop3con.user(username)
pop3conn.user(username)
pop3conn.pass_(password)

print(pop3conn)


