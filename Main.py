#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

from curses import echo
from distutils import command
import os
from time import sleep
from gpiozero import LED, DistanceSensor
import telebot
import sys
<<<<<<< HEAD
import board
import adafruit_dht
=======
import Adafruit_DHT
import RPi.GPIO as GPIO
>>>>>>> d249fbb04184ed0bfc18e959be66f33f84e0066d

API_TOKEN = '5113795649:AAHi0m4N7Zld-5jMurp_ObXCQJH_f7HGSOw'

bot = telebot.TeleBot(API_TOKEN)
led = LED(19)
sensor = DistanceSensor(echo=27, trigger=17)
sensorHyT = adafruit_dht.DHT11 #Adafruit_DHT.DHT11
dhtDevice = adafruit_dht.DHT11(board.D18, use_pulseio=False)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am LucadevBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")

@bot.message_handler(commands=['analiza'])
def sensor_onP(message): #Sensor de proximidad
    while True:
        dist = sensor.distance * 100
        if(dist <= 32):
            print("Dentro del if")
            bot.reply_to(message,"""Hay un objeto demsiado cerca!!! \nCUIDADO!!!""")
            sleep(1)
        else:
            print("No hay un objeto cerca.")
            sleep(1)
            

@bot.message_handler(commands=['temperatura'])
def sensor_onT(message): #Sensor de temperatura
<<<<<<< HEAD
    #while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )
        bot.reply_to(message,"""La temperatura es de """+str(temperature_c)+""" grados centígrados.""")

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        print("Hola")
        sleep(1)
        #continue
    except Exception as error:
        dhtDevice.exit()
        raise error
=======
    diccionarioLed1 = { #Contiene los pin del led de 7 segmentos
        'A': 5,
        'B': 7,
        'C': 8,
        'D': 10,
        'E': 13,
        'F': 15,
        'G': 16, }

    diccionarioLed2 = { #Contiene los pin del segundo led de 7 segmentos
        'A': 18,
        'B': 19,
        'C': 21,
        'D': 22,
        'E': 23,
        'F': 24,
        'G': 26, }

    numeros = { #Contiene los valores en binario para encender el led
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

    humedad = 0
    temperatura = 0
    while True:
        humedad, temperatura = Adafruit_DHT.read_retry(11, 3) #(tipo de sensor, pin)
        print ("Temp: {0:0.1f} ºC",temperatura) #Imprime la temperatura
        
        # Se divide el valor en unidad y decimal
        temp = int(temperatura)
        decima = numeros.get(str(int(temp / 10)))
        unidad = numeros.get(str(int(temp % 10)))
        
        
        piv = 0
        #for para encender los leds del 7 segmentos decimal
        for itera in diccionarioLed1:
            pin = diccionarioLed1.get(itera)
            bit = decima[piv]
            estado = GPIO.LOW
            if bit == "1":
                estado = GPIO.HIGH
            GPIO.output(pin, estado)
            piv = piv + 1
        
        #for para encender los leds del 7 segmentos unidad
        for itera in diccionarioLed1:
            pin = diccionarioLed2.get(itera)
            bit = unidad[piv]
            estado = GPIO.LOW
            if bit == "1":
                estado = GPIO.HIGH
            GPIO.output(pin, estado)
            piv = piv + 1
>>>>>>> d249fbb04184ed0bfc18e959be66f33f84e0066d

    sleep(1)

bot.infinity_polling()
