from datetime import datetime
ahora=datetime.now()
fecha=ahora.strftime('%d/%m/%Y')
archivo=open('ventas.txt','a')
TOTAL=0
def igv(a):
    subtotal=a * 0.18
    return subtotal
def Igv_total (a):
    subtotal=a *1.18
    return subtotal
def total(a,b):
    total=a*b
    return total
print('Ventas diarias')
print('--'*50)
for x in range (0,3):
    producto=str(input('Ingrese producto: '))
    precio=str(input('Ingrese precio: '))
    cantidad=str(input('Ingrese cantidad: '))
    archivo.write(cantidad+'\t'+producto+'\t'+precio +'\n')
    TOTAL=TOTAL + total(int(precio), int(cantidad))

archivo.write('Fecha: '+str(fecha)+'\n')
archivo.write('Subtotal: '+str(TOTAL)+'\n')
archivo.write('IGV: '+str(igv(TOTAL))+'\n')
archivo.write('Total: '+str(Igv_total(TOTAL))+'\n')
archivo.close