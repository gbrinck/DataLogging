#data logging en archivo en el procesador
import machine
import utime

datos = open('log01.txt', 'a')
datos.write('Hola mundo cruel 01!' + '\n')
datos.close()