import sys
import Adafruit_DHT

humedad = 0
temperatura = 0
while True:
    humedad, temperatura = Adafruit_DHT.read_retry(11, 4) #(tipo de sensor, pin)
    print ("Temp: {0:0.1f} ºC",temperatura)
    
#Codigo para enviar el dato al led de 7 segmentos
