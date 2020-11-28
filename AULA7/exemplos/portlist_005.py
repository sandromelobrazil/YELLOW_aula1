#!/usr/bin/python

portlist = set()
## pasando strings para definir range de portas


porttest1 = [ 'x', 'a', '1-20', '15-20', 'ab']

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
    
    else:
        print('Foi fornecido informacao de portas em formatao apropriado', _port)
        



print(portlist)
