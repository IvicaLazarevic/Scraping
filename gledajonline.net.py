#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'gledajonline.net.py'
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

def hdsaprevodom(godina):
    URL = f'https://gledajonline.net/year/toplista{godina}'
    RES = requests.get(URL)
    SOUP = BeautifulSoup(RES.content, 'html.parser')

    for film in SOUP.find_all('div', {'class':'img__wrap'}):
        print(f'[+] Naziv filma: {film.find("h5").text}')

if __name__ == '__main__':
    print('\n[+] Dobrodosli u skriptu koja radi scraping sajta gledajonline.net\n')
    GODINA = int(input('[+] Unesite godinu za koju zelite da prikazete najgledanije filmove(2000-2020): '))
    if GODINA < 2000 or GODINA > 2020:
        exit('[-] Niste pravilno uneli godinu! Unesite od 2000 do 2020!')
    else:
        print(f'[+] Prikazujemo TOP 50 najgledanijih u godini {GODINA}:\n')
    hdsaprevodom(GODINA)