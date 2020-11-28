#!/usr/bin/python

from threading import *
from datetime import datetime


def iplist(_iplist):
    with open(_iplist, 'r') as machines:
        while True:
            machine = machines.readline().strip("\n")

            if not machine:
                break
            print( '[+] - IP alvo:', machine)


time_start = datetime.now()
iplist('superiplist')
time_end = datetime.now()
time_total = time_end - time_start
print('[*] - Tempo total de execucao:', time_total)
