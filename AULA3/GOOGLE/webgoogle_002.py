#!/usr/bin/python

import webbrowser
import socket
import socks
from urllib.request import urlopen


googlehacking = 'https://www.google.com/search?q='

googledork = 'inurl:"/squid-reports/" AND intitle:"SARG reports"'



print("Connecting in TOR Network - Deep Weeb")
socks.setdefaultproxy(socks.PROXY_TYPE_SOCKS5,"localhost",9050)
socket.socket = socks.socksocket
url="http://icanhazip.com/"
request2 = urlopen(url)
print("My IP with TOR  is : {0}".format(request2.read()))
webbrowser.open_new_tab(googlehacking + googledork)

