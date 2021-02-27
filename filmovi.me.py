#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'filmovi.me.py'
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

def filmovi(stranica):
    for strana in range(0, stranica + 1):
        URL = f'https://www.filmovi.me/filmovi?page={strana}'
        RES = requests.get(URL)
        SOUP = BeautifulSoup(RES.content, 'html.parser')
        for film in SOUP.findAll('div', {'class':'opis'}):
            print(f'\n[+] Naziv filma: {film.find("a").text}')
            print(f'[+] Ocena filma: {film.find("span").text}')
            print(f'[+] Godina: {film.find("a", {"class":"godina"}).text}')
            print(f'[+] Link do filma: https://filmovi.me{film.find("a")["href"]}')

if __name__ == '__main__':
    print('\n[+] Dobrodosli u skriptu koja radi scraping sajta filmovi.me\n')
    BROJ_STRANICA = int(input('[+] Molimo vas unesite broj stranica za pretragu(24 filma po stranici): '))
    filmovi(BROJ_STRANICA)