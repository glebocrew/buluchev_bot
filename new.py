from telebot import *
from json import load
from random import choice

API = "8179785113:AAFKen3Z3wq-DEKjOI5RbeXiLLPKkkHt9Ls"

bot = TeleBot(API)
for x in range(100):
    bot.send_message(1696395843, text="Максим иди нахуй")