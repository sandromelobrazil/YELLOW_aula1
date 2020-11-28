
import socket
import sys

ip = "192.168.0.16"
port = 25
timeout_value = 2
verbose = 1
user = "msfadmin"

def func_xpl_vrfy():
    sys.stdout.flush()
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout_value)
    connect=s.connect((ip,port))
    banner=s.recv(1024)
    
    if verbose > 0:
        print("[*] Banner do Servidor STMP: '%s'") % (str(banner))
        command='RCPT ' + user + '\n'
    
    if verbose > 0:
        print("[*] Executando: %s") % (command)
        #print("[*] Entrada de teste %s de %s") % (str(username_list.index(user)),str( len(username_list)))
        #print("[*] Entrada de teste %s de %s") % (str(user))
        print("[*] Entrada de teste '%s' ") % (user)
        s.send(command)
        result=s.recv(1024)
        print((str(result)))

func_xpl_vrfy()

