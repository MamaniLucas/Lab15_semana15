nombre = input("Ingrese su nombre: ")
nota_1 = int(input("Ingrese la nota 1: "))
nota_2 = int(input("Ingrese la nota 2: "))
curso = str(input("Ingrese curso: "))


promedio = (nota_1 + nota_2)/2

aprobado = False

if promedio >= 13:
    aprobado = True

file = open("notas.txt", "w", '')

import datetime
def mostrarFecha():
    fecha = datetime.datetime.now()
    print(fecha.strftime("%H:%M:%S"))
mostrarFecha()
file.write("Nombre: " + nombre + " \n")
file.write("Nota 1: " + str(nota_1) + " \n")
file.write("Nota 2: " + str(nota_2) + " \n")
file.write("Promedio: " + str(promedio) + " \n")
file.write("Aprobado: " + str(aprobado) + " \n")
file.write('Fecha actual: '+ datetime+'\n')

file.close()





