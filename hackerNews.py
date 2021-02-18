#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'hackerNews.py'
__version__ = '0.1'
__site__ = 'pythonbytes.rs'

import sys
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

def hackerVesti():
    URL = 'https://news.ycombinator.com/rss'
    RES = requests.get(URL)
    SOUP = BeautifulSoup(RES.content, 'xml')

    for vest in SOUP.findAll('item'):
        print(f'[+] Naziv vesti: {vest.find("title").text}')
        print(f'[+] Datum izdavanja: {vest.find("pubDate").text}')
        print(f'[+] Link: {vest.find("link").text}\n')

    print('\n[+] Hvala vam sto ste koristili skriptu.')


if __name__ == '__main__':
    print('\n[+] Dobrodosli u skriptu koja radi scrap news.ycombinator.com\n')
    hackerVesti()