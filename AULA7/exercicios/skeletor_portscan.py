#!/usr/bin/python

### skeletor libraries
import argparse
import sys
import time
import nmap3
from pyfiglet import Figlet
from termcolor import colored
from datetime import datetime 

#### variaveis argpase - skeletor
nome_app = str(sys.argv[0])
msg_usage = "\n Usage: python3 " + nome_app + " -p  <ip alvo> \n" 
msg_domain = "Informe o dominio alvo" 
### variaveis do banner
msg_font=('puffy')
msg_banner="pyNMAP Ninja plu plus turbo" 
msg_banner_custom = Figlet(font=msg_font)
msg_banner_color=colored(msg_banner_custom.renderText(msg_banner), 'green')

#### Outras variaves
msg_ast=colored('[*]', 'yellow')
msg_int=colored('[!]', 'blue')
msg_ok=colored('[+]', 'green')
msg_fail=colored('[-]', 'red')

option_msg = ' ==================> AINDA NAO IMPLEMENTADO' 
msg_target = option_msg
msg_file = option_msg
msg_version = option_msg
msg_port = option_msg
msg_banner = option_msg
msg_vanilla = option_msg
msg_tcpsyn = option_msg
msg_banner = option_msg
msg_fingerprint = option_msg
msg_udp = option_msg


### skeletor

################ Inicio do seu codigo
###==> Auxiliares
### ===> Versao 
def versao():
    print(msg_banner_color)
    print(" -------------------------------------------------------------------> v.01")
    print()

### ===> Funcao checkip
### ===> Funcao ler arquivo
### ===> Funcao execucao com 1 thread
### ===> Funcao execucao com multipl<as thread

### ===> Funcao implementacao
def  linha(_cara, _number):
    print(_cara * _number)


def  naopronta():
    linha('=', 30)
    print()
    print(' AINDA EM DESENVOLVIMENTO ')
    print()
    linha('=', 30)

###==> Auxiliares

##### Funcao Vanilla SCAN -sT


##### Funcao Vanilla SCAN

##### Funcao TCP SYN -sS


##### Funcao TCP SYN

##### Funcao Banner Version -sV


##### Funcao Fingerprint -O


##### Funcao Fingreprint


##### Funcao UDP SCAN -sU


##### Funcao UDP SCAN




################ Fim do seu codigo
    

def func_main():
    option = argparse.ArgumentParser(description=msg_usage)
    option.add_argument("-t",'--target', dest="target",  help=msg_target)
    option.add_argument("-f",'--file', dest="file",  help=msg_file)
    option.add_argument("-p",'--port',  dest="ports",  help=msg_port)
    option.add_argument("-sT",'--vanilla',  dest="vanilla",  help=msg_vanilla, action='store_true')
    option.add_argument("-sS",'--tcpsyn',  dest="tcpsyn",  help=msg_tcpsyn, action='store_true')
    option.add_argument("-sV",'--banner',  dest="banner",  help=msg_banner, action='store_true')
    option.add_argument("-O",'--fingerprint',  dest="fingerprint",  help=msg_fingerprint, action='store_true')
    option.add_argument("-sU",'--udp',  dest="udp",  help=msg_udp, action='store_true')
    option.add_argument("-v",'--version',  dest="version",  help=msg_version, action='store_true')
    option_args = option.parse_args()
    
    if option_args.version:
        versao()

    if option_args.target == None:
        print(option.description)
        exit(0)

    targetip = option_args.target
    fileip = option_args.file
    
    if option_args.vanilla:
        naopronta()

    if option_args.tcpsyn:
        naopronta()

    if option_args.banner:
        naopronta()

    if option_args.fingerprint:
        naopronta()

    if option_args.udp:
        naopronta()





if __name__ == '__main__':
    func_main()

