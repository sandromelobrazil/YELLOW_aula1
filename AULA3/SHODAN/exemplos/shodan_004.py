#!/usr/bin/python

import shodan
shodan_mykey= '7TeyFZ8oyLulHwYUOcSPzZ5w3cLYib61'
shodan_api = shodan.Shodan(shodan_mykey)
shodan_host = shodan_api.host('3.220.87.155') 

def shodan_portscan(shodan_host):
    for _ports in shodan_host['data']:
        print("Portas identificadas:", _ports['port'])

shodan_portscan(shodan_host)


