#!/usr/bin/python

portlist = set()

porteste1 = [ '11-443', 'iE100', 'XYZ','1000', '30', '111', '11', '11', '11', '25', '22', '21', '22', '22', 'Zzz' ]

def testaporta(_ports):
    if _port.isdigit(): 
        portlist.add(int(_port))

    elif '-' in _port:
        portainicial, portafinal = _port.split('-')

        for _rangeport in range(int(portainicial), int(portafinal)+1):
            portlist.add(int(_rangeport))
    
    else:
        pass
    
    

for _port in porteste1:
    testaporta(_port)

print('=' * 50)
print(portlist)
print('=' * 50)


print('=' * 50)
print('=' * 50)
portlist2 = [ str(port) for port in portlist ]
listport = ','.join(portlist2)
print(listport)
print('=' * 50)
print('=' * 50)
