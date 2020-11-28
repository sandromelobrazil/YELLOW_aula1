#!/usr/bin/python

portlist = set()

porteste1 = [ '11-443', 'iE100', 'XYZ','1000', '30', '111', '11', '11', '11', '25', '22', '21', '22', '22', 'Zzz' ]

for _port in porteste1:
    if _port.isdigit(): 
        print('Adicionado ao SET:', _port)
        portlist.add(_port)

    elif '-' in _port:
       portainicial, portafinal = _port.split('-')
       print('Porta inicial:',portainicial)
       print('Porta Final:',portafinal)
    
    else:
        print('Nao eh digito, descartado:', _port)

print(portlist)
