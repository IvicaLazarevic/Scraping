#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'randomFilmovi.py'
__version__ = '0.1'
__site__ = 'pythonbytes.rs'

import sys
import random

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

TOP_250 = 'https://www.imdb.com/chart/top'
LISTA_TOP_250 = []

def randomTOP250():
    odgovor = requests.get(TOP_250)
    soup = BeautifulSoup(odgovor.text, 'html.parser')

    for tag in soup.select('td.titleColumn a'):
        LISTA_TOP_250.append(tag.text)


if __name__ == "__main__":
    randomTOP250()
    print(f'\n[+] Na izboru vam je ukupno: {len(LISTA_TOP_250)} naslova!')
    print(f'[+] Random izabran film je: {LISTA_TOP_250[random.randrange(0, len(LISTA_TOP_250))]}')

