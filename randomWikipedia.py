#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'randomWikipedia.py'
__version__ = '0.1'
__site__ = 'pythonbytes.rs'

import sys
import json
from subprocess import call

try:
    from selenium import webdriver
    import requests
    from colorama import Fore
except:
    call('pip3 install colorama requests selenium', shell=True)
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


def SELENIUM_WEB(URL):
    CHROME_DRAJVER = 'C:\chromedriver.exe' # OVO OBAVEZNO IZMENITI, I NAPISATI PRAVILNU PUTANJU GDE SE NALAZI CHROME DRIVER
    CHROME_OPCIJE = webdriver.ChromeOptions()
    CHROME_OPCIJE.add_experimental_option('excludeSwitches', ['enable-logging']) # NE OSTAVLJA LOGOVE U TERMINALU
    CHROME_OPCIJE.add_experimental_option('detach', True) # OSTAVLJA OTVOREN CHROME PROZOR NAKON ZAVRSETKA SKRIPTE
    DRAJVER = webdriver.Chrome(executable_path=CHROME_DRAJVER, options=CHROME_OPCIJE)
    DRAJVER.get(URL)

def randomWiki(BROJ_STRANICA):
    WIKI_URL = f'https://sr.wikipedia.org/w/api.php?action=query&list=random&rnnamespace=0&rnlimit={str(BROJ_STRANICA)}&format=json'
    res = requests.get(WIKI_URL)

    if res.ok:
        PODACI = res.json()['query']['random']
        print(f'[+] Generisan random broj stranica: {BROJ_STRANICA}\n')
        for broj, naziv in enumerate(PODACI):
            print(f'[{str(broj)}] - {naziv["title"]}')
        ODABIR_STRANICE = input('\n[+] Odaberite broj stranice koju zelite da vidite: ')
        try:
            PODACI[int(ODABIR_STRANICE)]['id']
        except Exception:
            exit('[!] Molimo vas, unesite pravilan broj za odabir!')

        OTVORITI_URL = f'https://sr.wikipedia.org/wiki?curid={str(PODACI[int(ODABIR_STRANICE)]["id"])}'
        SELENIUM_WEB(OTVORITI_URL)

if __name__ == '__main__':
    print('\n[+] Dobrodosli u skriptu koja vam prikazuje random clanke sa Vikipedije.')
    BROJ_STRANICA = input('\n[+] Molimo vas unesite broj random stranica za prikazivanje: ')
    randomWiki(BROJ_STRANICA)