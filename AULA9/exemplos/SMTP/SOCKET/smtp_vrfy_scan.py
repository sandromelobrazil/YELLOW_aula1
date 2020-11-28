
import socket

ip = "192.168.100.16"
port = 25
timeout_value = 2
verbose = 1
user = "msfadmin"

def func_xpl_vrfy():
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout_value)
    connect=s.connect((ip,port))
    banner=s.recv(1024)
    
    if verbose > 0:
        print("[*] Banner do Servidor STMP: '%s'") % (str(banner))
        command='VRFY ' + user + '\n'
    
    if verbose > 0:
        print("[*] Executando: %s") % (command)
        print("[*] Entrada de teste '%s' ") % (user)
        s.send(command)
        result=s.recv(1024)
        print((str(result)))

func_xpl_vrfy()

