#!/usr/bin/python

import shodan
shodan_mykey= '7TeyFZ8oyLulHwYUOcSPzZ5w3cLYib61'
shodan_api = shodan.Shodan(shodan_mykey)
shodan_host = shodan_api.host('3.220.87.155') 

print("IP alvo:", shodan_host['ip_str'])
print("Organizacao:", shodan_host.get('org','n/a'))
print("Sistema operacional:", shodan_host.get('os','n/a'))
