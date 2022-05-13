import RPi.GPIO as GPIO
import time

puerto1 = 17
puerto2 = 18
puerto3 = 27

# Esos elegi, pero sia ya estan ocupados pueden cambiar
GPIO.setmode(GPIO.BCM)
#led amarillo
GPIO.setup(puerto1, GPIO.OUT)
#led rojo
GPIO.setup(puerto2, GPIO.OUT)
#led verde
GPIO.setup(puerto3, GPIO.OUT)

while True:
  # La idea es estar monitoreando los sensors cada cierto intervalo de tiempo
  # si algun sensor se sale del umbral se cambaira a amarillo o rojo, mientras
  # en verde
  if():
    # Inserte funciones de lectura de sensores
    print('Alerta Critica')
    ledRojo()
  elif():
    # Inserte funciones de lectura de sensores
    print('Alerta')
    ledAmarillo()
  else:
    # Inserte funciones de lectura de sensores
    print('Todo ok')
    ledVerde()

def ledRojo():
  #apagar el led verde y amarillo
  GPIO.output(puerto3, GPIO.LOW)
  GPIO.output(puerto1, GPIO.LOW)
  #prender el led rojo
  GPIO.output(puerto2, GPIO.HIGH)
def ledAmarillo():
  #apagar el led verde y rojo
  GPIO.output(puerto3, GPIO.LOW)
  GPIO.output(puerto2, GPIO.LOW)
  #prender el led rojo
  GPIO.output(puerto1, GPIO.HIGH)
def ledVerde():
  #apagar el led rojo y amarillo
  GPIO.output(puerto2, GPIO.LOW)
  GPIO.output(puerto1, GPIO.LOW)
  #prender el led rojo
  GPIO.output(puerto3, GPIO.HIGH)