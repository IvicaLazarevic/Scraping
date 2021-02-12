#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'pasosSrbijeVisaFree.py'
__version__ = '0.1'
__site__ = 'pythonbytes.rs'

import sys
from subprocess import call

try:
    from selenium import webdriver
    from bs4 import BeautifulSoup
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

CHROME_DRAJVER = 'C:\chromedriver.exe'
VISA_URL = 'https://www.doyouneedvisa.com/passport/Serbia'

def visaSrbijaFree():
    CHROME_OPCIJE = webdriver.ChromeOptions()
    CHROME_OPCIJE.add_argument('--headless') # Ne prikazuje mi prozor Chroma
    CHROME_OPCIJE.add_experimental_option('excludeSwitches', ['enable-logging'])  # Sklanja mi output od drajvera na konzoli
    DRAJVER = webdriver.Chrome(executable_path=CHROME_DRAJVER, options=CHROME_OPCIJE)
    BROJ = 1
    try:
        DRAJVER.get(VISA_URL)
        soup = BeautifulSoup(DRAJVER.page_source, 'html.parser')
        INFO_PASOS = soup.find_all('div', class_='row rowranking')
        print('[+] Drzave za koje nije potrebna viza:\n')
        for INFO in INFO_PASOS:
            DRZAVA = INFO.find('div', class_='col-xs-5').text
            BROJ_DANA = INFO.find('div', class_='col-xs-4 detail-elem info-free').h6.text
            print(f'[{BROJ}] Drzava: {DRZAVA.strip()} dozvoljava boravak bez vize u duzini od {BROJ_DANA.replace("Days", "dana")}.')
            BROJ += 1

    except(KeyboardInterrupt):
        exit('[-] Skripta prekinuta sa radom!')
    except:
        pass


if __name__ == "__main__":
    print('\n[+] Dobrodosli u skriptu koja vam pokazuje za koje zemlje vam nije potrebna viza sa srpskim pasosom!')
    visaSrbijaFree()