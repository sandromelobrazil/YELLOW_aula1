#!/usr/bin/python

portlist = set()
## pasando strings
porttest1 = [ '1000','11', '11', '11', '111', '11', '22', '441']

for _port in porttest1:
    if  _port.isdigit():
        print('Isto eh um digito em formato de string:', _port)
        portlist.add(int(_port))

print(portlist)
