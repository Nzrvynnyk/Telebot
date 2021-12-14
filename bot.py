
import telebot
import wakeonlan
import os, sys
from subprocess import Popen
from telebot import types
import random


from telebot import types
bot = telebot.TeleBot('*************')


@bot.message_handler(commands=['help', 'wake'])
def send_welcome(message):
   msg = bot.send_message(message.chat.id, ' ^= ^`       ^b!    codex_bot!')


@bot.message_handler(commands=['setatus', 'item2'])
def run_block(run):
    p = Popen('D:\scripts\Telegrambot\test.py')
    msg = bot.send_message(run.chat.id, '')



@bot.message_handler(commands=['run', 'item1'])
def read_blocked(wake):
    b = Popen('/telbot/login3.py')
    bot.send_message(wake.chat.id, '     ^`     ^`        ^c ^i    ')




if __name__ == "__main__":
    bot.polling()

