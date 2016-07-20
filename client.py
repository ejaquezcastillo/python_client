import os

import time

try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import simplejson


def printMenu():
    print("WELCOME TO URL_SHORT")
    print("SELECT OPTION")
    print("1: ALL URLS")
    print("2: URL SHORT FROM ID")
    print("3: INFO FROM URL SHORT ID")
    print("4: All USERS")
    print("5: Lista de Estudiantes")
    print("0: Cerrar Cliente")


def all_urls():
    response = urllib2.urlopen("http://localhost:4567/json/allurls")
    data = simplejson.load(response)
    print (data)
    for i in data:
        print(i)
    time.sleep(6)

def short(id):
    response = urllib2.urlopen("http://localhost:4567/json/original/"+id)
    data = simplejson.load(response)
    print(data)
    time.sleep(6)

def info(id):
    response = urllib2.urlopen("http://localhost:4567/json/url/"+id)
    data = simplejson.load(response)
    print(data)
    time.sleep(6)

def all_users():
    response = urllib2.urlopen("http://localhost:4567/json/allusers")
    data = simplejson.load(response)
    print(data)
    for i in data:
        print(i)
    time.sleep(6)


def main():

    while True:
        print("=======================================================================================================")
        printMenu()
        select = input('\nSELECT OPTION: ')
        if (select == "1"):
            all_urls()
        if (select == "2"):
            id = str(input("ENTER ID:"))
            short(id)
        if (select == "3"):
            id = str(input("ENTER ID:"))
            info(id)
        if (select == "4"):
            all_users()
        if (select == "5"):
            ()
        if (select == "0"):
            print('\nTHANK YOU FOR USING OUR SERVICES!')
            break


if __name__ == '__main__':
    main()