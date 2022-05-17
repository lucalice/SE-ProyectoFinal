#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

from curses import echo
from distutils import command
import os
from time import sleep
from gpiozero import LED, DistanceSensor, LEDBoard
import telebot
import sys
import board
import adafruit_dht

API_TOKEN = '5113795649:AAHi0m4N7Zld-5jMurp_ObXCQJH_f7HGSOw'

bot = telebot.TeleBot(API_TOKEN)
led = LED(19)
leds = LEDBoard(0, 5, 6, 13)
leds2 = LEDBoard(12, 16, 20, 21)
sensor = DistanceSensor(echo=27, trigger=17)
temperature_f = 0
sensorHyT = adafruit_dht.DHT11 #Adafruit_DHT.DHT11
dhtDevice = adafruit_dht.DHT11(board.D18, use_pulseio=False)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
    Hola! Esta es la maceta Inteligente que se encargarà de mantenerte
        al tanto de tu planta. Saludos! (Versión 1)\
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
    #while True:
    try:
        # Print the values to the serial port
        temperature_c = dhtDevice.temperature
        global temperature_f 
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        print(
            "Temp: {:.1f} F / {:.1f} C    Humidity: {}% ".format(
                temperature_f, temperature_c, humidity
            )
        )
        prueba()
        centecima = getCentecima(temperature_c)
        decima = getDecima(temperature_c, centecima)
        numeros(centecima)
        numeros2(decima)
        
        bot.reply_to(message,"""La temperatura es de """+str(temperature_c)+""" grados centígrados.""")

    except RuntimeError as error:
        # Errors happen fairly often, DHT's are hard to read, just keep going
        print(error.args[0])
        sleep(1)
    except Exception as error:
        dhtDevice.exit()
        raise error

    sleep(1)
    
def getCentecima(numero):
    return numero // 10

def getDecima(numero,centecima):
    return - ((centecima * 10) - numero)
    
def numeros(num):
    if (num == 1):
        leds.value = (1, 0, 0, 0)
    elif(num == 2):
        leds.value = (0, 1, 0, 0)
    elif(num == 3):
        leds.value = (1, 1, 0, 0)
    elif(num == 4):
        leds.value = (0, 0, 1, 0)
    elif(num == 5):
        leds.value = (1, 0, 1, 0)
    elif(num == 6):
        leds.value = (0, 1, 1, 0)
    elif(num == 7):
        leds.value = (1, 1, 1, 0)
    elif(num == 8):
        leds.value = (0, 0, 0, 1)
    elif(num == 9):
        leds.value = (1, 0, 0, 1)
        
def numeros2(num):
    if (num == 1):
        leds2.value = (1, 0, 0, 0)
    elif(num == 2):
        leds2.value = (0, 1, 0, 0)
    elif(num == 3):
        leds2.value = (1, 1, 0, 0)
    elif(num == 4):
        leds2.value = (0, 0, 1, 0)
    elif(num == 5):
        leds2.value = (1, 0, 1, 0)
    elif(num == 6):
        leds2.value = (0, 1, 1, 0)
    elif(num == 7):
        leds2.value = (1, 1, 1, 0)
    elif(num == 8):
        leds2.value = (0, 0, 0, 1)
    elif(num == 9):
        leds2.value = (1, 0, 0, 1)
        
def prueba():
    print(temperature_f)

bot.infinity_polling()
