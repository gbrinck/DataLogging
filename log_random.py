#data logging mas datos...
import machine
import utime
import urandom

datos = open('log01.txt', 'w')
datos.write('Numeros random ' + '\n')
datos.close()

utime.sleep(1)

datos = open('log01.txt', 'a')
for eventos in range (1,101):
    azar = urandom.uniform(1,100)
    datos.write(str(eventos) + '; ' + str(azar) + '\n')
    datos.flush()
datos.close()