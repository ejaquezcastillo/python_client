try:
    import urllib.request as urllib2
except ImportError:
    import urllib2
import simplejson


def printMenu():
    print("WELCOME TO URL_SHORT")
    print("Option:")
    print("1: Obterner")
    print("2: Actualizar Estudiante")
    print("3: Obtener Estudiante dada una matricula")
    print("4: Borrar Estudiante")
    print("5: Lista de Estudiantes")
    print("0: Cerrar Cliente")


response = urllib2.urlopen("http://localhost:4567/json/admin/urls")
data = simplejson.load(response)
print (data)

def main():

    while True:
        printMenu()
        select = input('\nDigite una de las opciones: ')
        if (select == "1"):
            ()
        if (select == "2"):
            ()
        if (select == "3"):
            ()
        if (select == "4"):
            ()
        if (select == "5"):
            ()
        if (select == "0"):
            print('\n!Thank you for using our services!')
            break


if __name__ == '__main__':
    main()