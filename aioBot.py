import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command
from aiogram.types import FSInputFile, LinkPreviewOptions

from routers import router as main_router
from routers.questions_path.path import users

from config import *
from Buttons import *
from function import get_key
from animals import animals
from text import text
from answer import question_2


"""
1. Для того чтобы обновить или добавить вопрос откройте файл answer.py,
там будут дальнейшие инструкции!
2. Для того чтобы поменять описание животного, откройте файл text.py, 
найдите в массиве нужное животное и добавьте текст НЕ МЕНЯЯ КЛЮЧА. 
"""


bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(main_router)

@dp.message(Command("help"))
async def help(message: types.Message):
    text = """Вы попали на викторину, Ваше ТОТЕМНОЕ ЖИВОТНОЕ.
    В конце викторины мы опредилим, животное,
    с которым у Вас схожая энергетика 🐯🐻🦊🐱🐶🐼!
    Чтобы начать наберите команду /start!"""
    await message.answer(text=text)


@dp.message(CommandStart())
async def welcome(message: types.Message):
    user = message.from_user
    await message.answer(f'Приветствую Вас 😃, {user.full_name}')
    await message.answer(
        '<b>Вы попали на викторину, Ваше ТОТЕМНОЕ ЖИВОТНОЕ.'
        '\n В конце викторины мы определим, животное, с которым у Вас схожая энергетика 🐯🐻🦊🐱🐶🐼!</b>',
        parse_mode='html')
    await message.answer('Если готовы, нажмите "Начать викторину" и ответьте на несколько вопросов.',
                         reply_markup=btn_welcome())


@dp.message(F.text.in_(text_step_end))
async def step_end(message: types.Message):
    id = message.chat.id
    if not question_2:
        users[id]['point'] = 0
    if message.text == text_step_end[0]:
        users[id]['point'] += 5
    elif message.text == text_step_end[1]:
        users[id]['point'] += 10
    elif message.text == text_step_end[2]:
        users[id]['point'] += 15
    elif message.text == text_step_end[3]:
        users[id]['point'] += 20

    points = users[id]['point']
    rezult = users[id]['code']
    print('end2', users)
    links_text = (
        "https://moscowzoo.ru/about/guardianship"
        "\n"
        "t.me/Moscowzoo_official"
    )
    options_1 = LinkPreviewOptions(
        url="https://moscowzoo.ru/about/guardianship",
        prefer_large_media=True
    )

    text_id = get_key(text, points, rezult)
    image = get_key(animals, points, rezult)
    image_from_pc = FSInputFile(image)
    await message.answer_photo(image_from_pc)
    await message.answer("Ваше тотемное животное!")
    await message.answer(text_id)
    await message.answer(
        "Присоединитесь к сохранению исчезающих видов."
        "<b>\n Cтаньте опекуном.</b>", parse_mode='html'
    )
    await message.answer(
        f"Ссылка на сайт\n{links_text}",
        link_preciew_optins=options_1,
        reply_markup=btn_step_end()
    )


@dp.message(F.text.in_(['Поделиться']))
async def post(message: types.Message):
    pass


# @dp.message(F.text.in_(['Связаться с оператором']))
# async def statement(message: types.Message):
#     id = message.chat.id
#     points = users[id]['point']
#     rezult = users[id]['code']
#     text_id = get_key(text, points, rezult)
#     image = get_key(animals, points, rezult)
#     image_from_pc = FSInputFile(image)
#
#     links = ( "https://t.me/telegram")
#     options = LinkPreviewOptions(url="https://t.me/telegram")
#     await message.answer(
#         f"Для связи с оператором перейдите по ссылке\n {links}",
#         link_preview_options=options
#     )
#
#     await bot.send_message(
#         chat_id="https://t.me/telegram",
#         text=text_id
#     ),
#     await message.bot.send_photo(
#         chat_id="https://t.me/telegram",
#         photo=image_from_pc,
#     )


@dp.message(F.text.in_(['Оставить отзыв!']))
async def comment(message: types.Message):
    pass


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
