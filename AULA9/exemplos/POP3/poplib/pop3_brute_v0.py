#!/usr/bin/python3.7
from poplib import POP3

username='msfadmin'
password='msfadmin'

pop3conn = POP3('10.171.1.129', '110')
pop3conn.user(username)
pop3conn.pass_(password)

pop3srvmsg = pop3conn.getwelcome().decode('utf-8')

print('Connection successful')
print(pop3srvmsg)
print(pop3conn.stat())

pop3conn.quit()



