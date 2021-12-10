archivo_=open('archivo3.txt','a')
archivo=str(input('Ingrese una frase: '))
archivo_.write(archivo)
archivo_.close()
arch=open('archivo3.txt','r')
print(arch.read())
archivo_.close()

