import shodan
shodan_mykey= '7TeyFZ8oyLulHwYUOcSPzZ5w3cLYib61'
shodan_api = shodan.Shodan(shodan_mykey)
shodan_host = shodan_api.host('3.220.87.155') 

for info in shodan_host['vulns']:
    CVE = info.replace('!','')
    print("Vulnerabilidades:", info)
