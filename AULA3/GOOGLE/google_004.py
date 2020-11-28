#!/usr/bin/python

import time
import googlesearch

timesleep = 30

dorklist = [ 'intitle:"Sandro Melo"', 
        'intitle:"webcamXP 5"',
        'inurl:"webArch/mainFrame.cgi" + "Web Image Monitor"',
        'inurl:"/squid-reports/" AND intitle:"SARG reports"' ]

def google_query(_googledork):
    try:
        googlequery = googlesearch.search(_googledork, num_results=10)
        num =0
    
        print("Resultado com o Dork:", _googledork)
    
        for _link in googlequery:
            num += 1
            print("[+] - Link numero " + str(num), _link)

            if num == 10:
                print('==================== X ========================')
                print()
    except:
        print("Provavelmente o numero de consultas foi excedido - Erro 429")



for _dork in dorklist:
    google_query(_dork)
    print("Aguardando", timesleep,"para a proxima consulta")
    time.sleep(timesleep)


