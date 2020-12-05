#!/usr/bin/python
import paramiko
import sys
#os, socket 
#import itertools,string,crypt 


IPADDRESS="127.0.0.1"
SSHPORT=22
USERNAME = "root"
PASSWORD  = "xx"
 
 
ssh = paramiko.SSHClient()
ssh.load_system_host_keys()
ssh.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
 
try:
    ssh.connect(IPADDRESS , port=SSHPORT, username=USERNAME, password=PASSWORD)
    print "Connected successfully. Password = "+PASSWORD
except paramiko.AuthenticationException, error:
    print "Incorrect password: "+PASSWORD
except socket.error, error:
    print error
except paramiko.SSHException, error:
    print error
    print "Most probably this is caused by a missing host key"
#except Exception, error:
#    print "Unknown error: "+error
 
 
