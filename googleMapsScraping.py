#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'googleMapsScraping.py'
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
MAPS_URL = 'https://www.google.rs/maps/search/'

def googleMapsSelenium(PRETRAGA):
    CHROME_OPCIJE = webdriver.ChromeOptions()
    CHROME_OPCIJE.add_argument('--headless') # Ne prikazuje mi prozor Chroma
    CHROME_OPCIJE.add_experimental_option('excludeSwitches', ['enable-logging'])  # Sklanja mi output od drajvera na konzoli
    DRAJVER = webdriver.Chrome(executable_path=CHROME_DRAJVER, options=CHROME_OPCIJE)

    try:
        DRAJVER.get(MAPS_URL+PRETRAGA)
        soup = BeautifulSoup(DRAJVER.page_source, 'html.parser')
        INFO_FIRME = soup.find_all('div', class_='section-result-text-content')
        print(f'[+] Rezultati za prikazivanje: {len(INFO_FIRME)}')

        for firma in INFO_FIRME:
            IME_FIRME = firma.div.div.find('div', class_='section-result-title-container').h3.span.text
            OCENA = firma.div.div.find('div', class_='section-result-title-container').find('span', class_='cards-rating-score').text
            DETALJI_FIRME = firma.find('div', class_='section-result-details-container')
            DELATNOST_FIRME = DETALJI_FIRME.find('span', class_='section-result-details').text
            ADRESA_FIRME = DETALJI_FIRME.find('span', class_='section-result-location').text
            KONTATK_DETALJI = firma.find('div', class_='section-result-hours-phone-container')
            RADNO_VREME = KONTATK_DETALJI.find('span', class_='section-result-info section-result-opening-hours').text
            RADNO_VREME_ZAT = KONTATK_DETALJI.find('span', class_='section-result-info section-result-closed').text
            BROJ_TELEFONA = KONTATK_DETALJI.find('span', class_='section-result-info section-result-phone-number').text

            print(f'\n[+] Ime firme: {IME_FIRME}')
            if DELATNOST_FIRME not in ['']:
                print(f'[+] Delatnost firme: {DELATNOST_FIRME}')
            if ADRESA_FIRME not in ['']:
                print(f'[+] Adresa firme: {ADRESA_FIRME}')
            if 'Отворено' in RADNO_VREME or 'Отвара' in RADNO_VREME or 'Затвара' in RADNO_VREME or 'Open until' in RADNO_VREME or 'Opens at' in RADNO_VREME:
                print(f'[+] Radno vreme: {RADNO_VREME[:-2]}')
            if 'Затворено' in RADNO_VREME_ZAT or 'Closed' in RADNO_VREME_ZAT or 'Closed today' in RADNO_VREME_ZAT:
                print(f'[+] Radno vreme: {RADNO_VREME_ZAT[:-2]}')
            if '0' in BROJ_TELEFONA or '+' in BROJ_TELEFONA:
                print(f'[+] Broj telefona: {BROJ_TELEFONA[:-2]}')
            print(f'[+] Ocena: {OCENA}')


    except(KeyboardInterrupt):
        print('[-] Skripta prekinuta sa radom!')
    except:
        pass



if __name__ == '__main__':
    print('\n[+] Dobrodosli u skriptu koja radi scraping GoogleMaps!')
    print('[+] Skripta ne koristi API i radi scraping samo prve stranice rezultata!')
    PRETRAGA = input('\n[+] Molimo vas unesiti nazive za pretragu: ')
    googleMapsSelenium(PRETRAGA)


