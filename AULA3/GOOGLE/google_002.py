#!/usr/bin/python

import googlesearch

dorklist = [ 'intitle:"Sandro Melo"', 
        'intitle:"webcamXP 5"',
        'inurl:"webArch/mainFrame.cgi" + "Web Image Monitor"',
        'inurl:"/squid-reports/" AND intitle:"SARG reports"' ]

def google_query(_googledork):
    googlequery = googlesearch.search(_googledork, num_results=10)
    num =0
    
    for _link in googlequery:
        num += 1
        print("[+] - Link numero " + str(num), _link)
            

for _dork in dorklist:
    google_query(_dork)


