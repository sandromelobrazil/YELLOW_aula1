#!/usr/bin/python
import json
import shodan
shodan_mykey= '7TeyFZ8oyLulHwYUOcSPzZ5w3cLYib61'
shodan_api = shodan.Shodan(shodan_mykey)
shodan_host = shodan_api.host('3.220.87.155') 

mydictionary = shodan_host
shodan_json = json.dumps(mydictionary, indent = 6)
print(shodan_json)


