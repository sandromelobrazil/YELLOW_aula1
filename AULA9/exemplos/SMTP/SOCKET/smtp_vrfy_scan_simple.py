import socket

ip = "192.168.100.16"
port = 25
user = "msfadminxxx"
timeout_value = 2

def func_xpl_vrfy():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout_value)
    connect=s.connect((ip,port))
    banner=s.recv(1024)
    
    command='VRFY ' + user + '\n'
    s.send(command)
    result=s.recv(1024)
    return result

VRFYTEST=func_xpl_vrfy()
VRFYCODE = VRFYTEST.split(' ')

if "252" in str(VRFYCODE):
    print ("[*] BINDO - O nome do usuario '%s' eh uma conta valida!!! ") % (user)

if "550" in str(VRFYCODE):
    print ("[*] FALHOU - O nome do usuario '%s' NAOeh uma conta valida!!! ") % (user)


