#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'nacionalnaSluzba.py'
__version__ = '0.1'
__site__ = 'pythonbytes.rs'

import sys
import csv
from subprocess import call

try:
    import requests
    from bs4 import BeautifulSoup
    from colorama import Fore
except:
    call('pip3 install colorama requests bs4', shell=True)
    exit()


def logo():
    print(Fore.RED+"\n       __           __        ____      __        ")
    print(Fore.RED+"  ____/ /___ ______/ /_______/ __ \____/ /__  _____ ")
    print(Fore.RED+" / __  / __ `/ ___/ //_/ ___/ / / / __  / _ \/ ___/ ")
    print(Fore.RED+"/ /_/ / /_/ / /  / ,< / /__/ /_/ / /_/ /  __/ /     ")
    print(Fore.RED+"\__,_/\__,_/_/  /_/|_|\___/\____/\__,_/\___/_/      ")
    print(Fore.RED+"                                                \n")
    print(Fore.RED+'                               Naziv: '+ __scriptName__)
    print(Fore.RED+'                               Verzija: '+ __version__)
    print(Fore.RED+'                               Koder: '+ __coder__)
    print(Fore.RED+ '                               Sajt: ' + __site__+Fore.WHITE)

if sys.platform == 'linux' or sys.platform == 'linux2' or sys.platform == 'darwin':
    call('clear', shell=True)
    logo()
else:
    call('cls', shell=True)
    logo()

def sluzbaZaposljavanje():
    for strana in range(0, 20):
        URL = f'http://www.nsz.gov.rs/live/trazite-posao/poslovi-oglasi?pid={strana}'
        RES = requests.get(URL)
        SOUP = BeautifulSoup(RES.content, 'html.parser')

        for item in SOUP.find_all('div', {'class':'item-data'}):
            print(f'[+] Naziv radnog mesta: {item.find("cite").text}')
            print(f'[+] Adresa: {item.find("em").text}')
            print(f'[+] Datum postavljenog oglasa: {item.find("span").text}\n')
            CSV_UPIS.writerow([item.find('span').text, item.find('cite').text, item.find('em').text])
    print('[!] Proverite NacionalnaSluzbaZaposljavanje.csv za upisane rezultate!')

if __name__ == '__main__':
    print('\n[+] Dobrodosli u skriptu koja iscitava oglase za posao sa nsz.gov.rs\n')
    FAJL = open('NacionalnaSluzbaZaposljavanje.csv', 'w', newline='', encoding='utf-8')
    CSV_UPIS = csv.writer(FAJL)
    CSV_UPIS.writerow(['Datum', 'Radno mesto', 'Adresa'])
    sluzbaZaposljavanje()