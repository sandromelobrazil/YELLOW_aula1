#!/usr/bin/python

portlist = set()

porteste1 = [ 11, 100, 1000, 30, 111, 11, 11, 11, 25, 22, 21, 22, 22 ]

for _port in porteste1:
    print('Adicionado ao SET', _port)
    portlist.add(_port)

print(portlist)
