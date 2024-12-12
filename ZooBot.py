from telebot.async_telebot import AsyncTeleBot, types
import asyncio

from config import TOKEN
from function import get_key
from animals import animals
from text import text

bot = AsyncTeleBot(TOKEN)

users = {}

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
    await start_func(btn2)
    #bot.register_next_step_handler(message, start_func)
    print('aaa')


async def start_func(message):
    print('kkk')
    if message.text == 'На болоте с комарами!':
        rezult.clear()
        msg = rezult.append('swamp')
        #await bot.send_message(message.chat.id, "Ваш ответ принят!")
        await pre_herb(msg)

    elif message.text == 'На пляже или путешествуя по морю!':
        rezult.clear()
        msg =rezult.append('ocean')
        #msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
        await ocean(msg)

    elif message.text == 'В лесах или джунглях!':
        rezult.clear()
        msg =rezult.append('wood_jungles')
       # msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
        await pre_herb(msg)

    elif message.text == 'В степях или пустынях!':
        rezult.clear()
        msg =rezult.append('plain_dune')
       # msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
        await pre_herb(msg)

    elif message.text == 'В горах!':
        rezult.clear()
        msg =rezult.append('mount')
       # msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
        await pre_herb(msg)

    elif message.text == 'В пещере, где темно и сыро!':
        rezult.clear()
        msg =rezult.append('bats')
       # msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
        await step_1(msg)

    # else:
    #     msg = bot.send_message(message.chat.id, "Чтобы пройти дальше Вам надо ответить на вопрос!")
    #     await start(msg)
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
    if message.text == 'Холод':
        rezult.append('south')
        msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
        await south(msg)

    elif message.text == 'Жара':
        rezult.append('nord')
        msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
        await pre_herb(msg)

    else:
        msg = bot.send_message(message.chat.id, "Чтобы пройти дальше Вам надо ответить на вопрос!")
        await ocean(msg)
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
    if message.text == 'Купаться в море!':
        rezult.append('turtle')

    elif message.text == 'Ходить по пляжу!':
        rezult.append('flamingo')

    elif message.text == 'Лежать под пальмой!':
        rezult.append('stork')

    else:
        msg = bot.send_message(message.chat.id, "Чтобы пройти дальше Вам надо ответить на вопрос!")
        await south(msg)

    msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
    await step_1(msg)
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
    if message.text == 'Мне важно контролировать то что происходит вокруг меня!':
        rezult.append('predatory')
        if rezult[0] == 'wood_jungles':
            msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
            await wood(msg)
        elif rezult[0] == 'plain_dune':
            msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
            await plain_predatory(msg)
        elif rezult[0] == 'mount':
            msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
            await plain_predatory(msg)
        elif rezult[0] == 'swamp':
            msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
            await step_1(msg)
        elif rezult[1] == 'nord':
            msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
            await step_1(msg)

    elif message.text == 'Просто радуюсь жизни и получаю от неё удовольствие!':
        rezult.append('herbivores')
        if rezult[0] == 'wood_jungles':
            msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
            await wood(msg)
        elif rezult[0] == 'plain_dune':
            msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
            await plain_herbivores(msg)
        elif rezult[0] == 'mount':
            msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
            await step_1(msg)
        elif rezult[0] == 'swamp':
            msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
            await step_1(msg)
        elif rezult[1] == 'nord':
            msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
            await step_1(msg)

    else:
        msg = bot.send_message(message.chat.id, "Чтобы пройти дальше Вам надо ответить на вопрос!")
        await pre_herb(msg)
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
        msg = bot.send_message(message.chat.id, "Чтобы пройти дальше Вам надо ответить на вопрос!")
        await wood(msg)

    msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
    await step_1(msg)
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
    if message.text == 'Не суечусь, не тороплюсь, но когда надо всё сделаю!':
        rezult.append('cats')

    elif message.text == 'Мне нужно всё знать, и если за что-то возьмусь, то не отпущу!':
        rezult.append('falcon')

    elif message.text == 'Я очень трудолюбивый и добиваюсь своих целей!':
        rezult.append('dogs')

    else:
        msg = bot.send_message(message.chat.id, "Чтобы пройти дальше Вам надо ответить на вопрос!")
        await plain_predatory(msg)

    msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
    await step_1(msg)
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
    if message.text == 'incomplete_teeth':
        rezult.append('incomplete_teeth')
        msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
        await step_1(msg)

    elif message.text == 'birds':
        rezult.append('birds')
        msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
        await birds(msg)

    elif message.text == 'rodents':
        rezult.append('rodents')
        msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
        await step_1(msg)

    elif message.text == 'marsupials':
        rezult.append('marsupials')
        msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
        await step_1(msg)

    elif message.text == 'ungulates':
        rezult.append('ungulates')
        msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
        await step_1(msg)

    elif message.text == 'artiodactyls':
        rezult.append('artiodactyls')
        msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
        await step_1(msg)

    else:
        msg = bot.send_message(message.chat.id, "Чтобы пройти дальше Вам надо ответить на вопрос!")
        await plain_herbivores(msg)
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
        msg = bot.send_message(message.chat.id, "Чтобы пройти дальше Вам надо ответить на вопрос!")
        await birds(msg)

    msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
    await step_1(msg)
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
        msg = bot.send_message(message.chat.id, "Чтобы пройти дальше Вам надо ответить на вопрос!")
        await step_1(msg)

    msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
    await step_2(msg)


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
        msg = bot.send_message(message.chat.id, "Чтобы пройти дальше Вам надо ответить на вопрос!")
        await step_2(msg)

    msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
    await step_3(msg)
    print(points)


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
        msg = bot.send_message(message.chat.id, "Чтобы пройти дальше Вам надо ответить на вопрос!")
        await step_3(msg)

    msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
    await step_4(msg)


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
        msg = bot.send_message(message.chat.id, "Чтобы пройти дальше Вам надо ответить на вопрос!")
        await step_4(msg)

    msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
    await step_5(msg)


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
        msg = bot.send_message(message.chat.id, "Чтобы пройти дальше Вам надо ответить на вопрос!")
        await step_5(msg)

    msg = bot.send_message(message.chat.id, "Ваш ответ принят!")
    await step_end(msg)

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

    #image = get_key(animals, points, rezult)
    #text_id = get_key(text, points, rezult)
    #file = open(image, 'rb')
    #await bot.send_photo(message.chat.id, file)
    await bot.send_message(message.chat.id, "Ваше тотемное животное!")
    #await bot.send_message(message.chat.id, text_id)
    await bot.send_message(message.chat.id, "Присоединитесь к сохранению исчезающих видов – станьте опекуном.", reply_markup=markup)
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

    # elif message.text == 'Стать опекуном!':
    #     webbrowser.open('https://primer.ru')

    else:
        await bot.send_message(message.chat.id, "Выберите функцию!")
        await bot.register_next_step_handler(message, step_end)

    await bot.send_message(message.chat.id, "Нажмите подтвердить", reply_markup=markup)


asyncio.run(bot.polling(non_stop=True))
