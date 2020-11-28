import socket
from termcolor import colored

ip = "10.0.2.10"
port = 25
timeout_value = 3
user = "msfadmin"

def func_xpl_vrfy():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout_value)
    connect=s.connect((ip,port))
    banner=s.recv(1024)
    
    command = 'vrfy ' + user + '\n'
    cmd = command.encode()
    s.send(cmd)
    result=s.recv(1024)
    print(result)
    return result

#vrfytest = str(func_xpl_vrfy())
vrfytest = func_xpl_vrfy().encode()

vrfycode = vrfytest.split(' ')


if "252" in vrfycode:
    print (colored('[*]' ,'green'), "O nome do usuario", user, " eh uma conta valida: ") 

