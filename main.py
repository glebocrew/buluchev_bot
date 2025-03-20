from telebot import *
from json import load
from random import choice

import datetime


API = "8179785113:AAEd9lWmKhM9J9TKRvmiPcuOa7DXNi1UCzI"

bot = TeleBot(API)

word_site = "https://www.mit.edu/~ecprice/wordlist.10000"

res_path = "res/"

images = {
    ("коллега", "коллег", "колег", "колега"): {
        "img":"https://avatars.mds.yandex.net/i?id=0cab23f5f7d91bc7fb9970f7df947b82_l-5345374-images-thumbs&n=13",
        "phr":"Здравствуйте, коллега\!"
    },
    ("вероятность", "вероят"): {
        "img":"https://cs.hse.ru/mirror/org/persons/cimage/100060671",
        "phr":"Создайте абстрактное десятимерное пространство A, где у вас будут минусодномерные перегородки и стомерные шары\.Найдите вероятность, что я люблю геометрию если я опасный водитель."
    },
    ("excel", "exel", "модель", "модел", "таблица", "табл"):{
        "img":"https://myprepod.ru/img/201873018045671781.jpg",
        "phr":"Так\. Давайте я сейчас опущу проектор\. И мы с вами помоделируем в excel\. Вот, как вы видите, есть очень удобные функции данной программы\. Мы например можем подставить формулу\.Кстати, а вы знали что недавно добавили машинное обучение в эксель?"
    },
    ("z", "v", "слон", "гойда", "сво", "чил гай", "чил", "гай", "гол", "хуй", "пенис", "член", "анал", "сука", "бля", "нахуй"):{
        "img":"https://avatars.mds.yandex.net/i?id=b7147f6f34a73b8e0a13f822da5fd3efaa8f1b7096f4899d-12531500-images-thumbs&n=13",
        "phr":"Молодой человек\.Мне кажется вы слишком много говорите не по задаче\.Что это там за активность на первой парте? Помните же? Пропустили минуту, понимаем десять\!"
    },
    ("урок", "12"): {
        "img": "https://sun9-31.userapi.com/impg/_AKYb0SpitACgbbOegxn28vHpgJjeYqWJ1Ww4Q/xC-3U6RYAvI.jpg?size=180x180&quality=96&sign=760500bb687df0dab8dbc6a7dbe66992&type=album",
        "phr": "На сколько бы мне опоздать..."
    },
    ("самоненко", "илья", "юрьевич"):{
        "img":"https://pic.rutubelist.ru/video/86/4b/864babdada51fb76117cb38d3b10d7e5.jpg",
        "phr":"Тут уже я вмешаюсь\.Мой выход\!"
    }
}

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, text=f"Здравствуйте, коллега под номером {message.chat.id}\.Я не буду запоминать ваши имена\.Не по тому что мне лень, а потому что это будет нечестно проверять контрольные работы.")
    with open("chats.txt", "r+", encoding="utf-8") as file:
        readed = file.read().split(sep="\n")
        # print(readed)
        if not str(message.chat.id) in readed:
            file.write(f"{message.chat.id}\n")

@bot.message_handler(commands=['lesson'])
def random_text(message):
    with open("reasons.json", encoding="utf-8") as reasons:
        js = load(reasons)
    
    bot.send_photo(message.chat.id, photo="https://myprepod.ru/img/2017110220434484074.jpg",caption=f"Здравствуйте, коллеги\!\nСегодня я задержусь на работе из за того, что {choice(js)}\.\nНачнём урок на 30 минут позже, но я вас задержу на весь обед.")

@bot.message_handler(commands=["admin"])
def send(message):
    if message.chat.id == 1433192741:
        with open('chats.txt', 'r') as file:
            for chat in file.read().split(sep="\n"):
                if chat != '':
                        msg = message.text.split(sep = " ")
                        new_msg = ""
                        for x in msg[1:]:
                            new_msg += x + " "
                        bot.send_message(int(chat), text = new_msg)
            
@bot.message_handler()
def render_text(message):
    # print(message.text.lower())
    for word in message.text.lower().split(sep=" "):
        # print(word)
        if word == "подправим":
            # print(message.message_id)
            bot.send_message(message.chat.id, "Подправим чуть чуть")
            for id in range(message.message_id, message.message_id - 150, -1):
                try:
                    bot.delete_message(message.chat.id, id)
                except:
                    continue
        
        for phraze in images.keys():
            for one in phraze:
                if one in word:
                    bot.send_photo(message.chat.id, images[phraze]["img"], caption=images[phraze]["phr"])
                    # print(error)
                    # raise error  
                    # print(one, phraze, word)
                    # print(images[phraze]["phr"])    
                    break           


@bot.inline_handler(lambda query: True)
def inline_mode(inline_query):
    # print(message.text.lower())
    for word in inline_query.query.lower().split(sep=" "):
        for phraze in images.keys():
            for one in phraze:
                if one in word:
                    photo_result = telebot.types.InlineQueryResultPhoto(
                    id='1',  # Unique ID for the result
                    photo_url=images[phraze]["img"],  # URL of the photo
                    thumbnail_url=images[phraze]["img"],
                    caption=f'{images[phraze]["phr"]}',  # Add a caption here
                    parse_mode='MarkdownV2'  # Optional: Format the caption
                    )
                    bot.answer_inline_query(inline_query.id, [photo_result])
                    # print(error)
                    # raise error  
                    # print(one, phraze, word)
                    # print(images[phraze]["phr"])    
                    break           



if __name__ == '__main__':
    bot.infinity_polling()