import sys
import Adafruit_DHT
import RPi.GPIO as GPIO
import time
import argparse

humedad = 0
temperatura = 0
while True:
    humedad, temperatura = Adafruit_DHT.read_retry(11, 3) #(tipo de sensor, pin)
    print ("Temp: {0:0.1f} ºC",temperatura)
    
#Codigo para enviar el dato al led de 7 segmentos
diccionarioLed1 = {
    'A': 5,
    'B': 7,
    'C': 8,
    'D': 10,
    'E': 13,
    'F': 15,
    'G': 16, }

diccionarioLed2 = {
    'A': 18,
    'B': 19,
    'C': 21,
    'D': 22,
    'E': 23,
    'F': 24,
    'G': 26, }

numeros = {
    '0': '1111110',
    '1': '0110000',
    '2': '1101101',
    '3': '1111001',
    '4': '0110011',
    '5': '1011011',
    '6': '1011111',
    '7': '1110000',
    '8': '1111111',
    '9': '1110011', }

