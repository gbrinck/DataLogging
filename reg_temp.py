#Registrando la temperatura
import machine
import utime

led_int = machine.Pin(25, machine.Pin.OUT)
temp_int = machine.ADC(4)

def parpadeo(luz):
    for veces in range(luz):
        led_int(1)
        utime.sleep(.1)
        led_int(0)
        utime.sleep(.1)

reg_temp = open('datos.txt', 'a')
reg_temp.write('Hito ' + ';' + 'Temperatura' + '\n')
reg_temp.close()

factor = 3.3 / (65535)

utime.sleep(.2)

parpadeo(5)

reg_temp = open('datos.txt', 'a')

comienzo = utime.ticks_ms()

while True:
    lectura = temp_int.read_u16() * factor
    hito = round(((utime.ticks_ms()-comienzo)/1000),1)
    tempC = round((27 - (lectura - 0.706)/0.001721),1)
    reg_temp.write(str(hito) + '; ' + str(tempC) + '\n')
    reg_temp.flush()
    parpadeo(2)
    utime.sleep(5)
reg_temp.close()