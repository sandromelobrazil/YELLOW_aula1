#!/usr/bin/python

import shodan
shodan_mykey= '7TeyFZ8oyLulHwYUOcSPzZ5w3cLYib61'
shodan_api = shodan.Shodan(shodan_mykey)
shodan_host = shodan_api.host('3.220.87.155') 


def shodan_portscan(shodan_host):
    for _ports in shodan_host['data']:
        _port_target = _ports['port']
        print("Portas identificadas:", _port_target)
        for info in shodan_host['hostname']:
            #print(info['data'])
            print(info)

'''
        shodan_enumport = shodan_api.search('net:3.220.87.155  port:_porta_target')

        for info in shodan_enumport['matches']:
            print(info['data'])
'''

shodan_portscan(shodan_host)


