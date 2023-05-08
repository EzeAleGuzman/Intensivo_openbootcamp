#creo una agenda mediante un diccionario
agenda = {}

#creo una funcion para agregar contactos con sus telefonos mediante la consola
def agregar_contacto() :
    #le pido al usuario que me diga el nombre del nuevo contacto y lo agrego a la variable nombre
    nombre = input("Nombre de contacto: ")
    #le pido al usuario el numero y lo agrego a la variable telefono 
    Telefono = input("Telefono : ")
    #agrego los datos a mi agenda
    agenda[nombre]= Telefono
    print("Contacto Agregado")
    
#creo una funcion para buscar los contactos
def buscar_contactos():
    #le pido al usuario un nombre para la busqueda
    buscar = input("A quien quieres buscar: ")
    # utilizo el metodo get para iterar dentro de la agenda
    print(agenda.get(buscar,"sin resultado"))

#creo un menu de opciones con un bucle, que me permite utilizar las funciones de agregar contacto y buscar contacto, 
#como tambien salir del programa    
while True:
    print("Selecciona")
    print("1-Crear nuevo contacto")
    print("2- Buscar Contacto")
    print("3- salir")
    opcion = input("")
    if opcion == "1":
        agregar_contacto
    elif opcion == "2":
        buscar_contactos
    else:
        break