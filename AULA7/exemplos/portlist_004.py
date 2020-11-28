#!/usr/bin/python

portlist = set()
## pasando strings para definir range de portas


porttest1 = [ '1000','11', '11', '11', '111', '11', '22', '441', '10-1000', '1500-6000']

for _port in porttest1:
    if  _port.isdigit():
        print('Isto eh um digito em formato de string:', _port)
        portlist.add(int(_port))

    elif '-' in _port:
        portainicial, portafinal = _port.split('-')
        print('Porta inicial', portainicial)
        print('Porta Final', portafinal)

        for _rangeport in range(int(portainicial), int(portafinal)+1):
            portlist.add(_rangeport)

        



print(portlist)
