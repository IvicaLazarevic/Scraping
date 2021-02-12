#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'googleTranslate.py'
__version__ = '0.2'
__site__ = 'pythonbytes.rs'

import sys
from random import choice
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

def googlePrevod(POJAM):
    randomUserAgents = ['Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
                        'Opera/9.80 (X11; Linux x86_64; U; en-GB) Presto/2.2.15 Version/10.01']
    randomUserAgent = {'User-Agent': str(choice(randomUserAgents))}
    TRANSLATE_URL = f'https://translate.google.com/?sl=sr&tl=ru&text={POJAM}'
    RES = requests.get(TRANSLATE_URL, headers=randomUserAgent)
    SOUP = BeautifulSoup(RES.content, 'html.parser')

    for prevod in SOUP.find_all('div', {'class':'J0lOec'}):
        print(prevod.find('span', {'jsname':'W297wb'}).text)


if __name__ == '__main__':
    print('\n[+] Dobrodosli u skriptu koja sluzi za prevodjenje reci koristeci Google Translate.')
    POJAM = input('\n[+] Molimo vas unesite pojam koji zelite da prevedete sa srpskog na ruski:  ')
    googlePrevod(POJAM)