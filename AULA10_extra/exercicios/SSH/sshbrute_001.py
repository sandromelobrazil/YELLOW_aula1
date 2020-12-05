#!/usr/bin/python
import paramiko

target = '11.11.11.171'
portarget = 22
user = 'msfadmin'
pwd = 'msfadmin'

sshconn = paramiko.SSHClient()
sshconn.load_system_host_keys()
sshconn.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())

sshconn.connect(target,port=portarget, username=user, password=pwd)

print(sshconn)

sshconn.close()
