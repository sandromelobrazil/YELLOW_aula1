#!/usr/bin/python

import socks
import socket
from urllib.request import urlopen

googlehacking = 'https://www.google.com/search?q='

print("Connecting in TOR Network - Deep Weeb")
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,"localhost",9050)
socket.socket = socks.socksocket
url="http://icanhazip.com/"
request2 = urlopen(url)
print("My IP with TOR  is : {0}".format(request2.read()))

import mechanize
from mechanize import Browser

dorklist = [ 'intitle:"Sandro Melo"', 
        'intitle:"webcamXP 5"',
        'inurl:"webArch/mainFrame.cgi" + "Web Image Monitor"',
        'inurl:"/squid-reports/" AND intitle:"SARG reports"' ]

br = Browser()
print("BRowser")
print(br.open('http://icanhazip.com').read())


dorklist = [ 'intitle:"Sandro Melo"', 
        'intitle:"webcamXP 5"',
        'inurl:"webArch/mainFrame.cgi" + "Web Image Monitor"',
        'inurl:"/squid-reports/" AND intitle:"SARG reports"' ]

def google_mechanize(_googledork):
    print(_googledork)
    print(br.open(googlehacking + _googledork).read())
    



for _dork in dorklist:
    google_mechanize(_dork)


