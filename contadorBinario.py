import time
import RPi.GPIO as GPIO

#Configurando puertos Raspberry

#seteando modo BCM
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)


#seteando salidas
GPIO.setup(12,GPIO.OUT) #4
GPIO.setup(16,GPIO.OUT) #2
GPIO.setup(20,GPIO.OUT) #1

#we set everything on low at start
GPIO.output(12,GPIO.LOW)
GPIO.output(16, GPIO.LOW)
GPIO.output(20,GPIO.LOW)


#Definiendo funciones

def switchON(numero):
	'''
	función utilizada para encender los pines, segun la posición del valor binario
	:param numero: numero del pin a encender
	'''
    if(numero == 0):
        GPIO.output(20,GPIO.HIGH)
    if(numero == 1):
        GPIO.output(16,GPIO.HIGH)
    if(numero == 2):
        GPIO.output(12,GPIO.HIGH)

def switchOFF(numero):
	'''
	función utilizada para apagar los pines, segun la posición del valor binario
	:param numero: numero del pin a apagar
	'''
    if(numero == 0):
        GPIO.output(20,GPIO.LOW)
    if(numero == 1):
        GPIO.output(16,GPIO.LOW)
    if(numero == 2):
        GPIO.output(12,GPIO.LOW)

def setBinario(numero):
    #Obtenemos el binario y lo llenamos con 0 al inicio
    binario = bin(numero)[2:].zfill(3)
	
    #print("Colocando binario {0}".format(binario))
	
	#Recorriendo la posición de los valores, el digito de la posición 0 corresponde a la salida A
	#el valor de la posición 1, corresponde a la salida B. Y el valor de la posición 2, es la salida C
    for control, valor in enumerate(binario):
        #Si es 1 se coloca el pin en 1
		if(valor == '1'):
            switchON(control)
		#Si no es 1, se coloca el pin en 0
        else:
            switchOFF(control)


try:
    while True:
		#Conteo de 0 a 4
        for conteo in range(5):
            setBinario(conteo)
            time.sleep(2)

except KeyboardInterrupt:
    GPIO.cleanup()





    
