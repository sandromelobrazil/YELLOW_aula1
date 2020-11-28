#!/usr/bin/python

portlist = set()

porttest1 = [ 1000, 11, 33, 111 ]


for _port in porttest1:
    if int(_port):
        print('Eh um numero inteiro')
        portlist.add(int(_port))

    elif  _port.isdigit():
        print('Isto eh um digito em formato de string')
        portlist.add(int(_port))

print(portlist)
