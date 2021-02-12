#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'epicgamesPromocije.py'
__version__ = '0.1'
__site__ = 'pythonbytes.rs'

import sys
import json
from subprocess import call

try:
    import requests
    from colorama import Fore
except:
    call('pip3 install colorama requests', shell=True)
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


def epicgamesfree():
    FREE_GAMES_URL = 'https://store-site-backend-static.ak.epicgames.com/freeGamesPromotions?locale=en-US&country=RS&allowCountries=RS'
    res = requests.get(FREE_GAMES_URL)
    PODACI = res.json()

    for igra in PODACI['data']['Catalog']['searchStore']['elements']:
        print(f'[+] Naziv igre: {igra["title"]}')
        print(f'[+] Link ka igri: https://www.epicgames.com/store/en-US/product/{igra["productSlug"]}\n')


if __name__ == '__main__':
    print('\n[+] Ova skripta prikazuje igre na epicgames.com koje imaju promociju.\n')
    epicgamesfree()