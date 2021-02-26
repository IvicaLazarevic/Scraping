#!/usr/bin/env python3

__coder__ = 'Ivica Lazarevic'
__scriptName__ = 'navidiku.rs.py'
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

def navidikuRadio(drzava):
    URL = f'https://www.navidiku.rs/radio-stanice/{drzava}?sort=popularity'
    RES = requests.get(URL)
    SOUP = BeautifulSoup(RES.content, 'html.parser')
    for stanice in SOUP.findAll('div', {'class':'stations list'}):
        for stanica in stanice.findAll('li'):
            print(f'\n[+] Naziv stanice: {stanica.find("a", {"class":"name"}).text}')
            print(f'[+] Drzava: {stanica.find("span").text}')
            print(f'[+] Bitrate: {stanica.find("div", {"class":"bitrate"}).text}')
            print(f'[+] Ocena: {stanica.find("div", {"class":"summary"}).text}')

def navidikuTV():
    URL = 'https://www.navidiku.rs/tv-program/'
    RES = requests.get(URL)
    SOUP = BeautifulSoup(RES.content, 'html.parser')
    for kanali in SOUP.findAll('div', {'class':'tvb-box'}):
        print(f'\n[+] Tv Kanal: {kanali.find("h3").text}\n')
        for kanal in kanali.findAll('div', {'class':'tvb-inner'}):
            try:
                print(f'[+] {kanal.findAll("p")[0].text}')
                print(f'[+] {kanal.findAll("p")[1].text}')
                print(f'[+] {kanal.findAll("p")[2].text}')
                print(f'[+] {kanal.findAll("p")[3].text}')
                print(f'[+] {kanal.findAll("p")[4].text}')
            except:
                pass

def navidikuhoroskop():
    URL = 'https://www.navidiku.rs/horoskop/'
    RES = requests.get(URL)
    SOUP = BeautifulSoup(RES.content, 'html.parser')

    for znaci in SOUP.findAll('div', {'class':'horoscope-container'}):
        print(f'\n[+] Horoskopski znak: {znaci.findAll("h2")[0].text}')
        print(f'[+] Kratak opis: {znaci.findAll("p")[0].text.replace("»Više", "")}')
        print(f'\n[+] Horoskopski znak: {znaci.findAll("h2")[1].text}')
        print(f'[+] Kratak opis: {znaci.findAll("p")[1].text.replace("»Više", "")}')
        print(f'\n[+] Horoskopski znak: {znaci.findAll("h2")[2].text}')
        print(f'[+] Kratak opis: {znaci.findAll("p")[2].text.replace("»Više", "")}')
        print(f'\n[+] Horoskopski znak: {znaci.findAll("h2")[3].text}')
        print(f'[+] Kratak opis: {znaci.findAll("p")[3].text.replace("»Više", "")}')
        print(f'\n[+] Horoskopski znak: {znaci.findAll("h2")[4].text}')
        print(f'[+] Kratak opis: {znaci.findAll("p")[4].text.replace("»Više", "")}')
        print(f'\n[+] Horoskopski znak: {znaci.findAll("h2")[5].text}')
        print(f'[+] Kratak opis: {znaci.findAll("p")[5].text.replace("»Više", "")}')
        print(f'\n[+] Horoskopski znak: {znaci.findAll("h2")[6].text}')
        print(f'[+] Kratak opis: {znaci.findAll("p")[6].text.replace("»Više", "")}')
        print(f'\n[+] Horoskopski znak: {znaci.findAll("h2")[7].text}')
        print(f'[+] Kratak opis: {znaci.findAll("p")[7].text.replace("»Više", "")}')
        print(f'\n[+] Horoskopski znak: {znaci.findAll("h2")[8].text}')
        print(f'[+] Kratak opis: {znaci.findAll("p")[8].text.replace("»Više", "")}')
        print(f'\n[+] Horoskopski znak: {znaci.findAll("h2")[9].text}')
        print(f'[+] Kratak opis: {znaci.findAll("p")[9].text.replace("»Više", "")}')
        print(f'\n[+] Horoskopski znak: {znaci.findAll("h2")[10].text}')
        print(f'[+] Kratak opis: {znaci.findAll("p")[10].text.replace("»Više", "")}')
        print(f'\n[+] Horoskopski znak: {znaci.findAll("h2")[11].text}')
        print(f'[+] Kratak opis: {znaci.findAll("p")[11].text.replace("»Više", "")}')

def navidikuvreme():
    URL = 'https://www.navidiku.rs/vremenska-prognoza/'
    RES = requests.get(URL)
    SOUP =BeautifulSoup(RES.content, 'html.parser')

    for vreme in SOUP.findAll('tr'):
        print(f'\n[+] Grad: {vreme.findAll("td")[0].text.replace("Grad", "")}')
        print(f'[+] Vreme: {vreme.findAll("td")[1].text.replace("Vreme", "")}')
        print(f'[+] Temperatura: {vreme.findAll("td")[2].text.replace("Temperatura", "")}')
        print(f'[+] Pritisak: {vreme.findAll("td")[3].text.replace("Pritisak", "")}')
        print(f'[+] Vetar: {vreme.findAll("td")[4].text.replace("Vetar", "")}')


if __name__ == '__main__':
    print('\n[+] Dobrodosli u skriptu koja radi skraping sajta navidiku.rs\n')
    IZBOR = int(input('''[+] Ponudjene opcije:
    
    [1] - Radio Stanice
    [2] - Tv Program
    [3] - Horoskop
    [4] - Vremenska prognoza
    [0] - Izadji iz skripte
    
    [+] Molimo vas unesite opciju koju zelite: '''))

    if IZBOR not in [0, 1, 2, 3, 4]:
        exit('\n[-] Pogresno uneta opcija. Molimo vas pokusajte ponovo!')

    if IZBOR == 0:
        exit('\n[!] Hvala vam sto ste koristili skriptu!')

    if IZBOR == 1:
        izborR = int(input('''\n[+] Ponudjene drzave:
        
    [1] - Srbija
    [2] - BiH
    [3] - Hrvatska
    [4] - Severna Makedonija
    [5] - Crna Gora
    [6] - Slovenija
    [7] - Bugarska
    [8] - Rumunija
        
    [+] Molimo vas unesite drzavu za koju zelite da izlistate radio stanice: '''))

        if izborR not in [1, 2, 3, 4, 5, 6, 7, 8]:
            exit('\n[-] Pogresno uneta opcija. Molimo vas pokusajte ponovo!')

        if izborR == 1:
            DRZAVA = 'radio-stanice-srbija'

        if izborR == 2:
            DRZAVA = 'radio-stanice-bih'

        if izborR == 3:
            DRZAVA = 'radio-stanice-hrvatska'

        if izborR == 4:
            DRZAVA = 'radio-stanici-vo-severna-makedonija'

        if izborR == 5:
            DRZAVA = 'radio-stanice-crna-gora'

        if izborR == 6:
            DRZAVA = 'radio-stanice-slovenija'

        if izborR == 7:
            DRZAVA = 'radio-stanice-bugarska'

        if izborR == 8:
            DRZAVA = 'radio-stanice-rumunija'

        navidikuRadio(DRZAVA)

    if IZBOR == 2:
        navidikuTV()

    if IZBOR == 3:
        navidikuhoroskop()

    if IZBOR == 4:
        navidikuvreme()