#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'listaUFCturnira.py'
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

def UFC():
    UFC_WIKI = 'https://en.wikipedia.org/wiki/List_of_UFC_events'
    RES = requests.get(UFC_WIKI)
    SOUP = BeautifulSoup(RES.content, 'html.parser')

    for event in SOUP.find_all('table', {'id':'Past_events'}):
        for mec in event.findAll('tr'):
            try:
                print(f'\n[+] Dogadjaj broj: {mec.findAll("td")[0].text.strip()}')
                print(f'[+] Naziv dogadjaja: {mec.findAll("td")[1].text.strip()}')
                print(f'[+] Datum: {mec.findAll("td")[2].text.strip()}')
                print(f'[+] Mesto odrzavanja: {mec.findAll("td")[3].text.strip()}')
                print(f'[+] Lokacija: {mec.findAll("td")[4].text.strip()}')
                print(f'[+] Broj gledalaca: {mec.findAll("td")[5].text.strip()}')
            except:
                pass


if __name__ == '__main__':
    print('\n[+] Dobrodosli u skriptu koja prikazuje sve UFC turnire.')
    UFC()

