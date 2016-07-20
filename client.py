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
    print("4: ALL USERS")
    print("5: USER INFO")
    print("6: USER URLS HISTORY")
    print("7: NEW USER")
    print("8: NEW SHORT URL")
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

def user(username):
    response = urllib2.urlopen("http://localhost:4567/json/user/" +username)
    data = simplejson.load(response)
    print(data)
    time.sleep(6)


def user_urls(username):
    response = urllib2.urlopen("http://localhost:4567/json/" + username +"/urls")
    data = simplejson.load(response)
    print(data)
    for i in data:
        print(i)
    time.sleep(6)

def new_user(username, firstname, lastname, password):
    response = urllib2.urlopen("http://localhost:4567/json/newuser?username="  + username + "&fisrtname=" + firstname + "&lastname=" + lastname + "&password=" + password)
    url = ("http://localhost:4567/json/newuser?username="  + username + "&fisrtname=" + firstname + "&lastname=" + lastname + "&password=" + password)
    print ("SUCCESSFULLY!!!")

def new_url(url, username):
    response = urllib2.urlopen("http://localhost:4567/json/newurl?url=" + url + "&username=" + username)
    data = simplejson.load(response)
    print(data)
    print("SUCCESSFULLY!!!")




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
            username = str(input("ENTER USER:"))
            user(username)

        if (select == "6"):
            username = str(input("ENTER USER:"))
            user_urls(username)

        if (select == "7"):
            username = str(input("ENTER USERNAME:"))
            firsname = str(input("ENTER FIRSTNAME:"))
            lastname = str(input("ENTER LASTNAME:"))
            password = str(input("ENTER PASSWORD:"))
            new_user(username, firsname, lastname, password)

        if (select == "8"):
            url = str(input("ENTER URL:"))
            username  = str(input("ENTER USERNAME:"))
            new_url(url, username)

        if (select == "0"):
            print('\nTHANK YOU FOR USING OUR SERVICES!')
            break


if __name__ == '__main__':
    main()

