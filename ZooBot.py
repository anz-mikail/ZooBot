from telebot.async_telebot import AsyncTeleBot
from telebot import types
import asyncio

import webbrowser
import sqlite3

from config import TOKEN
from function import get_key
from animals import animals
from text import text

bot = AsyncTeleBot(TOKEN)

users = {}

# @bot.message_handler(commands=['hi'])
# def hi(message):
#     conn = sqlite3.connect('BdZoo.sql')
#     cur = conn.cursor()
#
#     cur.execute('CREATE TABLE IF NOT EXISTS users (id int auto_increment primary key, name varchar(50), rezult varchart(10))')
#     conn.commit()
#     cur.close()
#     conn.close()
#
#     bot.send_message()


@bot.message_handler(commands=['start'])
async def welcome(message):
    global rezult, points
    user = message.from_user
    id = message.chat.id
    users[id] = {}
    users[id]['first_name'] = user.first_name
    users[id]['last_name'] = user.last_name
    users[id]['code'] = ['a', 'a']
    users[id]['point'] = 0
    points = users[id]['point']
    rezult = users[id]['code']
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.InlineKeyboardButton(text="Пройти тест"))
    await bot.send_message(id, f'Приветствую Вас, {user.first_name} {user.last_name}')
    await bot.send_message(id, "<b>Это тест который определит Ваше ТОТЕМНОЕ ЖИВОТНОЕ</b>", parse_mode='html')
    await bot.send_message(id, "Если хотите начать, нажмите Пройти тест и ответьте на несколько вопросов.", reply_markup=markup)
    print(users)



@bot.message_handler(func=lambda message: message.text == 'Пройти тест')
async def start(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('На болоте с комарами!')
    btn2 = types.KeyboardButton('На пляже или путешествуя по морю!')
    markup.row(btn1, btn2)

    btn3 = types.KeyboardButton('В лесах или джунглях!')
    btn4 = types.KeyboardButton('В степях или пустынях!')
    markup.row(btn3, btn4)

    btn5 = types.KeyboardButton('В горах!')
    btn6 = types.KeyboardButton('В пещере, где темно и сыро!')
    markup.row(btn5, btn6)

    await bot.send_message(message.chat.id, "На какой местности вы предпочитаете проводить время?", reply_markup=markup)
    await bot.register_next_step_handler(message, start_func)



async def start_func(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Продолжить'))

    if message.text == 'На болоте с комарами!':
        rezult.clear()
        rezult.append('swamp')
        await bot.register_next_step_handler(message, pre_herb)

    elif message.text == 'На пляже или путешествуя по морю!':
        rezult.clear()
        rezult.append('ocean')
        await bot.register_next_step_handler(message, ocean)

    elif message.text == 'В лесах или джунглях!':
        rezult.clear()
        rezult.append('wood_jungles')
        await bot.register_next_step_handler(message, pre_herb)

    elif message.text == 'В степях или пустынях!':
        rezult.clear()
        rezult.append('plain_dune')
        await bot.register_next_step_handler(message, pre_herb)

    elif message.text == 'В горах!':
        rezult.clear()
        rezult.append('mount')
        await bot.register_next_step_handler(message, pre_herb)

    elif message.text == 'В пещере, где темно и сыро!':
        rezult.clear()
        rezult.append('bats')
        await bot.register_next_step_handler(message, step_1)

    else:
        await bot.send_message(message.chat.id, "Чтобы пройти дальше Вам надо ответить на вопрос!")
        await bot.register_next_step_handler(message, start)

    await bot.send_message(message.chat.id, 'Нажмите продолжить!', reply_markup=markup)
    print(users)


async def ocean(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Жара')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Холод')
    markup.row(btn2)

    await bot.send_message(message.chat.id, "Чего вы не любите больше?", reply_markup=markup)
    await bot.register_next_step_handler(message, ocean_func)


async def ocean_func(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Продолжить'))
    if message.text == 'Холод':
        rezult.append('south')
        await bot.register_next_step_handler(message, south)

    elif message.text == 'Жара':
        rezult.append('nord')
        await bot.register_next_step_handler(message, pre_herb)

    else:
        await bot.send_message(message.chat.id, "Чтобы пройти дальше Вам надо ответить на вопрос!")
        await bot.register_next_step_handler(message, ocean)

    await bot.send_message(message.chat.id, "Нажмите продолжить!", reply_markup=markup)
    print(users)


async def south(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Купаться в море!')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Ходить по пляжу!')
    markup.row(btn2)
    btn3 = types.KeyboardButton('Лежать под пальмой!')
    markup.row(btn3)

    await bot.send_message(message.chat.id, "Чем вы предпочитаете заниматься на пляже?", reply_markup=markup)
    await bot.register_next_step_handler(message, south_func)


async def south_func(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Продолжить'))
    if message.text == 'Купаться в море!':
        rezult.append('turtle')

    elif message.text == 'Ходить по пляжу!':
        rezult.append('flamingo')

    elif message.text == 'Лежать под пальмой!':
        rezult.append('stork')

    else:
        await bot.send_message(message.chat.id, "Чтобы пройти дальше Вам надо ответить на вопрос!")
        await bot.register_next_step_handler(message, south)

    await bot.send_message(message.chat.id, "Нажмите продолжить!", reply_markup=markup)
    await bot.register_next_step_handler(message, step_1)
    print(users)

async def pre_herb(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Мне важно контролировать то что происходит вокруг меня!')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Просто радуюсь жизни и получаю от неё удовольствие!')
    markup.row(btn2)

    await bot.send_message(message.chat.id, "Какое утверждение вам ближе?", reply_markup=markup)
    await bot.register_next_step_handler(message, pre_herb_func)


async def pre_herb_func(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Продолжить'))
    if message.text == 'Мне важно контролировать то что происходит вокруг меня!':
        rezult.append('predatory')
        if rezult[0] == 'wood_jungles':
            await bot.register_next_step_handler(message, wood)
        elif rezult[0] == 'plain_dune':
            await bot.register_next_step_handler(message, plain_predatory)
        elif rezult[0] == 'mount':
            await bot.register_next_step_handler(message, plain_predatory)
        elif rezult[0] == 'swamp':
            await bot.register_next_step_handler(message, step_1)
        elif rezult[1] == 'nord':
            await bot.register_next_step_handler(message, step_1)

    elif message.text == 'Просто радуюсь жизни и получаю от неё удовольствие!':
        rezult.append('herbivores')
        if rezult[0] == 'wood_jungles':
            await bot.register_next_step_handler(message, wood)
        elif rezult[0] == 'plain_dune':
            await bot.register_next_step_handler(message, plain_herbivores)
        elif rezult[0] == 'mount':
            await bot.register_next_step_handler(message, step_1)
        elif rezult[0] == 'swamp':
            await bot.register_next_step_handler(message, step_1)
        elif rezult[1] == 'nord':
            await bot.register_next_step_handler(message, step_1)

    else:
        await bot.send_message(message.chat.id, "Чтобы пройти дальше Вам надо ответить на вопрос!")
        await bot.register_next_step_handler(message, pre_herb)

    await bot.send_message(message.chat.id, "Нажмите продолжить!", reply_markup=markup)
    print(rezult)
    print(users)

async def wood(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Там где чисто!')
    btn2 = types.KeyboardButton('Там где меня не заметят!')
    markup.row(btn1, btn2)

    btn3 = types.KeyboardButton('Лягу там где придётся!')
    btn4 = types.KeyboardButton('Вырою себе блиндаж!')
    markup.row(btn3, btn4)

    btn5 = types.KeyboardButton('Поселюсь на дереве!')
    markup.row(btn5)

    await bot.send_message(message.chat.id, "Представьте что вы живёте в лесу или джунглях, как вы сделаете себе жилище?", reply_markup=markup)
    await bot.register_next_step_handler(message, wood_func)


async def wood_func(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Продолжить'))
    if message.text == 'Там где чисто!':
        if rezult[1] == 'predatory':
            rezult.append('cats')
        elif rezult[1] == 'herbivores':
            rezult.append('parrot')

    elif message.text == 'Там где меня не заметят!':
        if rezult[1] == 'predatory':
            rezult.append('scaly')
        elif rezult[1] == 'herbivores':
            rezult.append('artiodactyls')

    elif message.text == 'Лягу там где придётся!':
        if rezult[1] == 'predatory':
            rezult.append('dogs')
        elif rezult[1] == 'herbivores':
            rezult.append('primates')

    elif message.text == 'Вырою себе блиндаж!':
        if rezult[1] == 'predatory':
            rezult.append('raccoon')
        elif rezult[1] == 'herbivores':
            rezult.append('rodents')

    elif message.text == 'Поселюсь на дереве!':
        if rezult[1] == 'predatory':
            rezult.append('owl')
        elif rezult[1] == 'herbivores':
            rezult.append('sparrow')

    else:
        await bot.send_message(message.chat.id, "Чтобы пройти дальше Вам надо ответить на вопрос!")
        await bot.register_next_step_handler(message, wood)

    await bot.send_message(message.chat.id, "Нажмите продолжить!", reply_markup=markup)
    await bot.register_next_step_handler(message, step_1)
    print(rezult)
    print(users)


async def plain_predatory(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Не суечусь, не тороплюсь, но когда надо всё сделаю!')
    markup.row(btn1)
    btn2 = types.KeyboardButton('Мне нужно всё знать, и если за что-то возьмусь, то не отпущу!')
    markup.row(btn2)
    btn3 = types.KeyboardButton('Я очень трудолюбивый и добиваюсь своих целей!')
    markup.row(btn3)

    await bot.send_message(message.chat.id, "Какое утверждение вам ближе?", reply_markup=markup)
    await bot.register_next_step_handler(message, plain_predatory_func)


async def plain_predatory_func(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Продолжить'))
    if message.text == 'Не суечусь, не тороплюсь, но когда надо всё сделаю!':
        rezult.append('cats')

    elif message.text == 'Мне нужно всё знать, и если за что-то возьмусь, то не отпущу!':
        rezult.append('falcon')

    elif message.text == 'Я очень трудолюбивый и добиваюсь своих целей!':
        rezult.append('dogs')

    else:
        await bot.send_message(message.chat.id, "Чтобы пройти дальше Вам надо ответить на вопрос!")
        await bot.register_next_step_handler(message, plain_predatory)

    await bot.send_message(message.chat.id, "Нажмите продолжить!", reply_markup=markup)
    await bot.register_next_step_handler(message, step_1)
    print(rezult)
    print(users)

async def plain_herbivores(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('incomplete_teeth')
    btn2 = types.KeyboardButton('birds')
    markup.row(btn1, btn2)

    btn3 = types.KeyboardButton('rodents')
    btn4 = types.KeyboardButton('marsupials')
    markup.row(btn3, btn4)

    btn5 = types.KeyboardButton('ungulates')
    btn6 = types.KeyboardButton('artiodactyls')
    markup.row(btn5, btn6)

    await bot.send_message(message.chat.id, "Выберите A2 B2 C2 D2", reply_markup=markup)
    await bot.register_next_step_handler(message, plain_herbivores_func)


async def plain_herbivores_func(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Продолжить'))
    if message.text == 'incomplete_teeth':
        rezult.append('incomplete_teeth')
        await bot.register_next_step_handler(message, step_1)

    elif message.text == 'birds':
        rezult.append('birds')
        await bot.register_next_step_handler(message, birds)

    elif message.text == 'rodents':
        rezult.append('rodents')
        await bot.register_next_step_handler(message, step_1)

    elif message.text == 'marsupials':
        rezult.append('marsupials')
        await bot.register_next_step_handler(message, step_1)

    elif message.text == 'ungulates':
        rezult.append('ungulates')
        await bot.register_next_step_handler(message, step_1)

    elif message.text == 'artiodactyls':
        rezult.append('artiodactyls')
        await bot.register_next_step_handler(message, step_1)

    else:
        await bot.send_message(message.chat.id, "Чтобы пройти дальше Вам надо ответить на вопрос!")
        await bot.register_next_step_handler(message, plain_herbivores)

    await bot.send_message(message.chat.id, "Нажмите продолжить!", reply_markup=markup)
    print(users)


async def birds(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('cancerous')
    btn2 = types.KeyboardButton('chicken')
    markup.row(btn1, btn2)

    btn3 = types.KeyboardButton('crane')
    btn4 = types.KeyboardButton('goose')
    markup.row(btn3, btn4)

    btn5 = types.KeyboardButton('pigeon')
    btn6 = types.KeyboardButton('turaco')
    markup.row(btn5, btn6)

    await bot.send_message(message.chat.id, "Выберите A2 B2 C2 D2", reply_markup=markup)
    await bot.register_next_step_handler(message, birds_func)


async def birds_func(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Продолжить'))
    if message.text == 'cancerous':
        rezult.append('cancerous')

    elif message.text == 'chicken':
        rezult.append('chicken')

    elif message.text == 'crane':
        rezult.append('crane')

    elif message.text == 'goose':
        rezult.append('goose')

    elif message.text == 'pigeon':
        rezult.append('pigeon')

    elif message.text == 'turaco':
        rezult.append('turaco')

    else:
        await bot.send_message(message.chat.id, "Чтобы пройти дальше Вам надо ответить на вопрос!")
        await bot.register_next_step_handler(message, birds)

    await bot.send_message(message.chat.id, "Нажмите продолжить!", reply_markup=markup)
    await bot.register_next_step_handler(message, step_1)
    print(users)


#-------------------------------------------------------------------
async def step_1(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('A')
    btn2 = types.KeyboardButton('B')
    markup.row(btn1, btn2)

    btn3 = types.KeyboardButton('C')
    btn4 = types.KeyboardButton('D')
    markup.row(btn3, btn4)

    await bot.send_message(message.chat.id, "step_1", reply_markup=markup)
    await bot.register_next_step_handler(message, step_1_func)


async def step_1_func(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Продолжить'))
    global points
    if message.text == 'A':
        points = 0
        points += 5

    elif message.text == 'B':
        points = 0
        points += 10

    elif message.text == 'C':
        points = 0
        points += 15

    elif message.text == 'D':
        points = 0
        points += 20

    else:
        await bot.send_message(message.chat.id, "Чтобы пройти дальше Вам надо ответить на вопрос!")
        await bot.register_next_step_handler(message, step_1)

    await bot.send_message(message.chat.id, "Нажмите продолжить!", reply_markup=markup)
    await bot.register_next_step_handler(message, step_2)


async def step_2(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('A')
    btn2 = types.KeyboardButton('B')
    markup.row(btn1, btn2)

    btn3 = types.KeyboardButton('C')
    btn4 = types.KeyboardButton('D')
    markup.row(btn3, btn4)

    await bot.send_message(message.chat.id, "step_2", reply_markup=markup)
    await bot.register_next_step_handler(message, step_2_func)


async def step_2_func(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Продолжить'))
    global points
    if message.text == 'A':
        points += 5

    elif message.text == 'B':
        points += 10

    elif message.text == 'C':
        points += 15

    elif message.text == 'D':
        points += 20

    else:
        await bot.send_message(message.chat.id, "Чтобы пройти дальше Вам надо ответить на вопрос!")
        await bot.register_next_step_handler(message, step_2)

    await bot.send_message(message.chat.id, "Нажмите продолжить!", reply_markup=markup)
    await bot.register_next_step_handler(message, step_3)


async def step_3(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('A')
    btn2 = types.KeyboardButton('B')
    markup.row(btn1, btn2)

    btn3 = types.KeyboardButton('C')
    btn4 = types.KeyboardButton('D')
    markup.row(btn3, btn4)

    await bot.send_message(message.chat.id, "step_3", reply_markup=markup)
    await bot.register_next_step_handler(message, step_3_func)


async def step_3_func(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Продолжить'))
    global points
    if message.text == 'A':
        points += 5

    elif message.text == 'B':
        points += 10

    elif message.text == 'C':
        points += 15

    elif message.text == 'D':
        points += 20

    else:
        await bot.send_message(message.chat.id, "Чтобы пройти дальше Вам надо ответить на вопрос!")
        await bot.register_next_step_handler(message, step_3)

    await bot.send_message(message.chat.id, "Нажмите продолжить!", reply_markup=markup)
    await bot.register_next_step_handler(message, step_4)


async def step_4(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('A')
    btn2 = types.KeyboardButton('B')
    markup.row(btn1, btn2)

    btn3 = types.KeyboardButton('C')
    btn4 = types.KeyboardButton('D')
    markup.row(btn3, btn4)

    await bot.send_message(message.chat.id, "step_4", reply_markup=markup)
    await bot.register_next_step_handler(message, step_4_func)


async def step_4_func(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Продолжить'))
    global points
    if message.text == 'A':
        points += 5

    elif message.text == 'B':
        points += 10

    elif message.text == 'C':
        points += 15

    elif message.text == 'D':
        points += 20

    else:
        await bot.send_message(message.chat.id, "Чтобы пройти дальше Вам надо ответить на вопрос!")
        await bot.register_next_step_handler(message, step_4)

    await bot.send_message(message.chat.id, "Нажмите продолжить!", reply_markup=markup)
    await bot.register_next_step_handler(message, step_5)


async def step_5(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('A')
    btn2 = types.KeyboardButton('B')
    markup.row(btn1, btn2)

    btn3 = types.KeyboardButton('C')
    btn4 = types.KeyboardButton('D')
    markup.row(btn3, btn4)

    await bot.send_message(message.chat.id, "step_5", reply_markup=markup)
    await bot.register_next_step_handler(message, step_5_func)


async def step_5_func(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Продолжить'))
    global points
    if message.text == 'A':
        points += 5

    elif message.text == 'B':
        points += 10

    elif message.text == 'C':
        points += 15

    elif message.text == 'D':
        points += 20

    else:
        await bot.send_message(message.chat.id, "Чтобы пройти дальше Вам надо ответить на вопрос!")
        await bot.register_next_step_handler(message, step_5)

    await bot.send_message(message.chat.id, "Нажмите продолжить!", reply_markup=markup)
    await bot.register_next_step_handler(message, step_end)

    print(points)


async def step_end(message):
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Повторить ещё')
    btn2 = types.KeyboardButton('Поделиться')
    markup.row(btn1, btn2)

    btn3 = types.KeyboardButton('Связаться с оператором')
    btn4 = types.KeyboardButton('Оставить отзыв!')
    markup.row(btn3, btn4)

    btn5 = types.KeyboardButton('Стать опекуном!')
    markup.row(btn5)

    image = get_key(animals, points, rezult)
    text_id = get_key(text, points, rezult)
    file = open(image, 'rb')
    await bot.send_photo(message.chat.id, file)
    await bot.send_message(message.chat.id, "Ваше тотемное животное!")
    await bot.send_message(message.chat.id, text_id, reply_markup=markup)
    await bot.send_message(message.chat.id, "Присоединитесь к сохранению исчезающих видов – станьте опекуном.")
    await bot.register_next_step_handler(message, step_end_func)


async def step_end_func(message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Подтвердить'))

    if message.text == 'Повторить ещё':
        await bot.register_next_step_handler(message, start)

    elif message.text == 'Поделиться':
        await bot.register_next_step_handler(message, start)

    elif message.text == 'Связаться с оператором':
        await bot.register_next_step_handler(message, start)

    elif message.text == 'Оставить отзыв!':
        await bot.register_next_step_handler(message, start)

    elif message.text == 'Стать опекуном!':
        webbrowser.open('https://primer.ru')

    else:
        await bot.send_message(message.chat.id, "Выберите функцию!")
        await bot.register_next_step_handler(message, step_end)

    await bot.send_message(message.chat.id, "Нажмите подтвердить", reply_markup=markup)


asyncio.run(bot.polling(non_stop=True))
