#data logging en archivo en el procesador
import machine
import utime

datos = open('log01.txt', 'r')
print (datos.read())
datos.close()