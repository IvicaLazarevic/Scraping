#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'googleTranslate.py'
__version__ = '0.1'
__site__ = 'pythonbytes.rs'

import sys
from subprocess import call

try:
    from bs4 import BeautifulSoup
    from selenium import webdriver
    from colorama import Fore
except:
    call('pip3 install colorama selenium bs4', shell=True)
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
    CHROME_OPCIJE = webdriver.ChromeOptions()
    #CHROME_OPCIJE.add_argument('--lang=ru')
    #CHROME_OPCIJE.add_argument('headless')
    CHROME_OPCIJE.add_experimental_option('excludeSwitches', ['enable-logging'])
    CHROME_OPCIJE.add_experimental_option('detach', True)
    DRAJVER = webdriver.Chrome(executable_path=CHROME_DRAJVER, options=CHROME_OPCIJE)
    TRANSLATE_URL = f'https://translate.google.com/?sl=sr&tl=ru&text={POJAM}%20&op=translate'
    DRAJVER.get(TRANSLATE_URL)
    SOUP = BeautifulSoup(DRAJVER.page_source, 'html.parser')

    for prevod in SOUP.find_all('div', {'class':'J0lOec'}):
        print(prevod.find('span', {'jsname':'W297wb'}).text)



if __name__ == '__main__':
    CHROME_DRAJVER = 'C:\chromedriver.exe'
    print('\n[+] Dobrodosli u skriptu koja sluzi za prevodjenje reci koristeci Google Translate.')
    POJAM = input('\n[+] Molimo vas unesite pojam koji zelite da prevedete sa srpskog na ruski:  ')
    googlePrevod(POJAM)