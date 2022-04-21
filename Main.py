#!/usr/bin/python

# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

from curses import echo
from distutils import command
import os
from time import sleep
from gpiozero import LED, DistanceSensor
import telebot

API_TOKEN = '5113795649:AAHi0m4N7Zld-5jMurp_ObXCQJH_f7HGSOw'

bot = telebot.TeleBot(API_TOKEN)
led = LED(19)
sensor = DistanceSensor(echo=18, trigger=17)

# Handle '/start' and '/help'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, """\
        Hi there, I am LucadevBot.
        I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
        """)


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
#@bot.message_handler(func=lambda message: True)
#def echo_message(message):
#    bot.reply_to(message, message.text)

@bot.message_handler(commands=['analiza'])
def sensor_on(message):
    while True:
        dist = sensor.distance * 100
        if(dist <= 10):
            return "Hay un objeto muy cerca de tu planta. Ten cuidado!!!"


bot.infinity_polling()