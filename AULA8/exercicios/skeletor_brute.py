#!/usr/bin/python

### skeletor libraries
import argparse
import time
from pyfiglet import Figlet
from termcolor import colored
from datetime import datetime 
from threading import *
import ipaddress as ipaddress
from concurrent.futures import ThreadPoolExecutor

#### variaveis argpase - skeletor
nome_app = str(sys.argv[0])
msg_usage = "\n Usage: python3 " + nome_app + " -sT  -t  <ip alvo> -p <portas> \n" 
msg_domain = "Informe o dominio alvo" 
### variaveis do banner
msg_font=('puffy')
msg_banner="pyNMAP Ninja plu plus turbo" 
msg_banner_custom = Figlet(font=msg_font)
msg_banner_color=colored(msg_banner_custom.renderText(msg_banner), 'green')

#### Outras variave
msg_ast=colored('[*]', 'yellow')
msg_int=colored('[!]', 'blue')
msg_ok=colored('[+]', 'green')
msg_ok1=colored('[+]', 'green')
msg_ok2=colored('[+] ==>', 'cyan')
msg_fail=colored('[-]', 'red')

option_msg = ' ==================> AINDA NAO IMPLEMENTADO' 
msg_target = 'Define o IP alvo'
msg_file = 'Informe o arquivo com a lista de IP'
msg_version = 'Inform a versao do Script'
msg_port = 'Informe a porta/s alvo -p 22 ou uma range -p 22-100'
msg_banner = 'Possibilita a leitura de Banners'
msg_vanilla = 'Varredura Vanilla Scan'
msg_tcpsyn = 'Varredura TCP Steulth' 
msg_fingerprint = 'Fingerprint - Detecao do SO' 
msg_udp = 'Varredura UDP'

################################################# BRUTEFORCE FUNCTIONS

    

################################################# BRUTEFORCE FUNCTIONS
def func_main():
    option = argparse.ArgumentParser(description=msg_usage)
    option.add_argument("-t",'--target', dest="target",  help=msg_target)
    option.add_argument("-f",'--file', dest="file",  help=msg_file)
    option.add_argument("-e",'--expn',  dest="expn",  help=msg_vanilla, action='store_true')
    option.add_argument("-r",'--rcpt',  dest="rcpt",  help=msg_tcpsyn, action='store_true')
    option.add_argument("-v",'--vrfy',  dest="vrfy",  help=msg_banner, action='store_true')
    option.add_argument("-v",'--version',  dest="version",  help=msg_version, action='store_true')
    option_args = option.parse_args()

    targetip = option_args.target
    fileip = option_args.file


    if option_args.version:
        version()
    
    if option_args.vrfy:
        print('ALVO: ', targetip)
        print('PORTAS:',portas)
        #nmap_vanilla(targetip,'-F')

        if option_args.file != None:
            run_threads(option_args.file)
            for _ip in lista_ip_testados:
                print('=' * 60)
                print('[*] ---> IP ALVO:', _ip)
                print('=' * 60)
                nmap_vanilla(_ip, '-p'+portas)
                print()

        else:
            nmap_vanilla(targetip, '-p'+portas)


if __name__ == '__main__':
    func_main()

