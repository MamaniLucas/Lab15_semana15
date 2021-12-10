print("Sea cordialmente bienvenido a registro y lectura")
print("¿Que desea hacer primero?")
opcionMenu =int(input(">>Selecciona una opción<< \n 1-Registro\n 2-lectura \n "))

while opcionMenu != 0:
    if opcionMenu == 1:
        nombre= str(input("Ingrese su nombre completo: "))
        edad= str(input("Edad: "))
        fecha = str(input("Fecha de nacimiento: "))
        file = open("texto.txt", "w")
        file.write("Nombre: " + nombre +" \n")
        file.write("Edad: " + edad + " \n")
        file.write("Fecha: " + fecha + " \n")
        

    elif opcionMenu == 2:
        texto = input("Escribe un texto: ")
        file = open("texto.txt", "a")
        file.write("Texto: " + texto)
        file=open("texto.txt", "p")
        print (file.read())

    else:
        file=open("texto.txt", "r")
        print (file.read())

    opcionMenu = int(input("Menu principal: \n 1- Ver registro \n 2- Ver Lectura \n"))






