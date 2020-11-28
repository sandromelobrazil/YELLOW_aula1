#!/usr/bin/python

import webbrowser

googlehacking = 'https://www.google.com/search?q='

googledork = 'inurl:"/squid-reports/" AND intitle:"SARG reports"'

webbrowser.open_new_tab(googlehacking + googledork)



