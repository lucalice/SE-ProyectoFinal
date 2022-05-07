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
import board
import adafruit_dht

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

    sleep(1)

bot.infinity_polling()
