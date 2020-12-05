#!/usr/bin/python
import paramiko
import sys

IPADDRESS="192.168.100.16"
SSHPORT=22
USERNAME = "msfadmin"
PASSWORD = "msfadmin"
 
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
 
try:
    ssh.connect(IPADDRESS , port=SSHPORT, username=USERNAME, password=PASSWORD)
    print "BINGO a senha do " + USERNAME + " eh: " + PASSWORD
except paramiko.AuthenticationException, error:
    print "FALHOU - A senha do usuario: " + USERNAME + " nao eh:  " + PASSWORD
except socket.error, error:
    print error
except paramiko.SSHException, error:
    print error
    print "Alguma coisa errada com a  host key"
 
 
