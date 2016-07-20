import time
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import simplejson

#MENU
def printMenu():
    print("WELCOME TO URL_SHORT")
    print("\nSELECT OPTION")
    print("1: ALL URLS")
    print("2: URL SHORT FROM ID")
    print("3: INFO FROM URL SHORT ID")
    print("4: ALL USERS")
    print("5: USER INFO")
    print("6: USER URLS HISTORY")
    print("7: NEW USER")
    print("8: NEW SHORT URL")
    print("0: Cerrar Cliente")

#FUNCION NO.1 - DEVUELVE TODOS LOS URLS CONSULTADOS
def all_urls():
    response = urllib2.urlopen("http://localhost:4567/json/allurls")
    data = simplejson.load(response)
    print (data)
    for i in data:
        print(i)
    time.sleep(6)

#FUNCION NO.2 - DEVUELVE UN URL-SHORT DADO UN ID
def short(id):
    response = urllib2.urlopen("http://localhost:4567/json/original/"+id)
    data = simplejson.load(response)
    print(data)
    time.sleep(6)

#FUNCION NO.3 - DEVUELVE INFORMACION DEL USER CREADOR DE UN URL-SHORT DADO UN ID
def info(id):
    response = urllib2.urlopen("http://localhost:4567/json/url/"+id)
    data = simplejson.load(response)
    print(data)
    time.sleep(6)

#FUNCION NO.4 - DEVUELVE TODOS LOS USUARIOS
def all_users():
    response = urllib2.urlopen("http://localhost:4567/json/allusers")
    data = simplejson.load(response)
    print(data)
    for i in data:
        print(i)
    time.sleep(6)

#FUNCION NO.5 - DEVUELVE INFORMACION DE USUARIO DADO UN USERNAME
def user(username):
    response = urllib2.urlopen("http://localhost:4567/json/user/" +username)
    data = simplejson.load(response)
    print(data)
    time.sleep(6)

#FUNCION NO.6 - DEVUELVE INFORMACION HISTORICA DADO UN USUARIO
def user_urls(username):
    response = urllib2.urlopen("http://localhost:4567/json/" + username +"/urls")
    data = simplejson.load(response)
    print(data)
    for i in data:
        print(i)
    time.sleep(6)

#FUNCION NO.7. - CREA UN NUEVO USUARIO DADO USERNAME, FIRSTNAME, LASTNAME, PASSWORD
def new_user(username, firstname, lastname, password):
    response = urllib2.urlopen("http://localhost:4567/json/newuser?username="  + username + "&firstname=" + firstname + "&lastname=" + lastname + "&password=" + password)
    print ("\nSUCCESSFULLY!!!")
    time.sleep(6)
#FUNCION NO.8 - CREAR UN NUEVO URL A UN USERNAME
def new_url(url, username):
    response = urllib2.urlopen("http://localhost:4567/json/newurl?url=" + url + "&username=" + username)
    print("\nSUCCESSFULLY!!!")
    time.sleep(6)


#FUNCION SELECTOR DEL MENU
def main():

    while True:
        print("=======================================================================================================")
        printMenu()
        select = input('\nSELECT OPTION:')
        #ALL URLS
        if (select == "1"):
            all_urls()
        #URL SHORT FROM ID
        if (select == "2"):
            id = str(input("ENTER ID:"))
            short(id)
        #INFO FROM URL SHORT ID
        if (select == "3"):
            id = str(input("ENTER ID:"))
            info(id)
        #ALL USERS
        if (select == "4"):
            all_users()
        #USER INFO
        if (select == "5"):
            username = str(input("ENTER USER:"))
            user(username)
        #USER URLS HISTORY
        if (select == "6"):
            username = str(input("ENTER USER:"))
            user_urls(username)
        #NEW USER
        if (select == "7"):
            username = str(input("ENTER USERNAME:"))
            firsname = str(input("ENTER FIRSTNAME:"))
            lastname = str(input("ENTER LASTNAME:"))
            password = str(input("ENTER PASSWORD:"))
            new_user(username, firsname, lastname, password)
        #NEW SHORT URL
        if (select == "8"):
            url = str(input("ENTER URL:"))
            username  = str(input("ENTER USERNAME:"))
            new_url(url, username)

        if (select == "0"):
            print('\nTHANK YOU FOR USING OUR SERVICES!')
            break


if __name__ == '__main__':
    main()

