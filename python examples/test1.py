from random import randrange, choice

personas = ['danna', 'michelle', 'andy']

def menu():
    print("------- Menu ------")
    print("1. agregar persona")
    print("2. ver personas:")
    print("3. escoger a la persona ganadora de mi kokoro:")
    opcion = int(input("Escoge una opcion :"))

    if opcion == 1 :
        nombre = input("ingrese un nombre:")
        addPeople(personas, nombre)
        menu()
    elif opcion == 2 :
        seePeople(personas)
        menu()
    elif opcion == 3 :
        PeopleAleatory(personas)
        menu()
    else:
        print("ningun caso")

def seePeople(person):
    for x in person:    
        print(x)

def addPeople(person,name):
    person.append(name)
    print("se ha agregado esta persona : "+name)

def PeopleAleatory(person):
    print("la persona que le gustas es :")
    print(choice(person))


menu()