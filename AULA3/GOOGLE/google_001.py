#!/usr/bin/python

import googlesearch

google_dork = 'intitle:"Sandro Melo"'
googlequery = googlesearch.search(google_dork, num_results=10)
num =0
for _link in googlequery:
    print("[+] - Link numero " + str(num), _link)
