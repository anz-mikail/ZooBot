import asyncio
import logging
import time
import datetime

from cryptography.fernet import Fernet

from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.types import FSInputFile, LinkPreviewOptions
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from routers import router as main_router
from routers.questions_path.path import users

from config import *
from Buttons import *
from function import get_key
from animals import animals
from text import text
from answer import question_2
from logger import BotLogger




"""
1. Для того чтобы обновить или добавить вопрос откройте файл answer.py,
там будут дальнейшие инструкции!
2. Для того чтобы поменять описание животного, откройте файл text.py, 
найдите в массиве нужное животное и добавьте текст НЕ МЕНЯЯ КЛЮЧА.
3. В файле function.py хранится логика расчёта.
4. В файле review.txt  хранятся отзывы пользователей.
5. В файле config.py хранится ТОКЕН и настроена очередь вопросов.
6. Логика расчёта заключается в том что, схожие животные по параметрам 
лежат в одной папке
- блок вопросов routers/questions_path приводит к папке.
- блок вопросов routers/questions_points добавляет балла. 
7. В файле Bot.log хранятся логи 
"""


bot = Bot(token=TOKEN)
dp = Dispatcher()

dp.include_router(main_router)

logger = BotLogger(__name__)

key = Fernet.generate_key()
cipher_suite = Fernet(key)


async def encrypt_and_log_data(data):
    encrypted_data = cipher_suite.encrypt(data.encode())
    logger.info("Зашифрованные данные: %s", encrypted_data)


async def decrypt_data(encrypted_data):
    decrypted_data = cipher_suite.decrypt(encrypted_data)
    return decrypted_data.decode()


class PostState(StatesGroup):
    id = State()

# Функция, которая сохраняет отзыв пользователя в файл review.txt
def CreateReview(user, review, rezult):
    time = datetime.datetime.now()
    format_time = time.strftime("%m-%d %H:%M")
    f = open('review.txt', 'a', encoding='utf8')
    f.write(f'{format_time}, {user} оценил викторину: {review}, результат викторины: {rezult}\n')
    f.close()


# ID чата оператора технической поддержки,
# туда же уходит сообщение если случилась ошибка
TechnicalChat = 6620559407


# Функция, которая отправляет сообщение в технический чат.
async def send_TechnicalChat(message):
    await bot.send_message(TechnicalChat, message)


@dp.message(Command("help"))
async def help(message: types.Message):
    text = """Вы попали на викторину, Ваше ТОТЕМНОЕ ЖИВОТНОЕ.
    В конце викторины мы определим животное,
    с которым у Вас схожая энергетика 🐯🐻🦊🐱🐶🐼!
    Чтобы начать наберите команду /start!"""
    await message.answer(text=text)


@dp.message(CommandStart())
async def welcome(message: types.Message):
    user = message.from_user
    logger.log_info(f"Пользователь {user.full_name} запустил бота с командой /start")
    await message.answer(f'Приветствую Вас 😃, {user.full_name}')
    await message.answer(
        '<b>Вы попали на викторину, Ваше ТОТЕМНОЕ ЖИВОТНОЕ.'
        '\n В конце викторины мы определим животное, с которым у Вас схожая энергетика 🐯🐻🦊🐱🐶🐼!</b>',
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
    links_text = (
        "https://moscowzoo.ru/about/guardianship"
        "\n"
        "t.me/Moscowzoo_official"
    )
    options_1 = LinkPreviewOptions(
        url="https://moscowzoo.ru/about/guardianship",
        prefer_large_media=True
    )
    try:
        start_time = time.time()
        text_id = get_key(text, points, rezult)
        image = get_key(animals, points, rezult)
        end_time = time.time()
        logger.log_info(f"Операция создания ключа длилась{end_time - start_time} секунд")

        logger.log_info(f"Пользователь {message.from_user.full_name} "
                        f"завершил викторину с результатом {text_id}")
        users[id]['text'] = text_id
        users[id]['image'] = image

        start_time1 = time.time()
        image_from_pc = FSInputFile(image)
        await message.answer_photo(image_from_pc)
        await message.answer("Ваше тотемное животное!")
        await message.answer(text_id)
        end_time1 = time.time()
        logger.log_info(f"операция по отправке картинки и "
                        f"текста длилась {end_time1 - start_time1} секунд")

        await message.answer(
            "Присоединяйтесь к сохранению исчезающих видов животных."
            "<b>\nCтаньте опекуном.</b>", parse_mode='html'
        )
        await message.answer(
            f"Подробная информация о программе Стать опекуном на сайте\n{links_text}",
            link_preciew_optins=options_1,
            reply_markup=btn_step_end()
        )
    except Exception as e:
        logger.log_error(f"Ошибка: {str(e)}")
        await send_TechnicalChat("Произошла ошибка в боте!")


@dp.message(F.text == 'Поделиться')
async def post_1(message: types.Message, state: FSMContext):
    await state.set_state(PostState.id)
    await message.answer(
        'Введите ID чата телеграмм',
    )


@dp.message(PostState.id)
async def post_2(message: types.Message, state: FSMContext):
    try:
        id = message.chat.id
        chat_id = message.text
        image_from_pc = FSInputFile(users[id]['image'])
        await bot.send_message(
            chat_id=chat_id,
            text=f"Участник: {users[id]['name']}\n"
                 f"Тотемное животное: {users[id]['text']}",
        )
        await message.bot.send_photo(
            chat_id=chat_id,
            photo=image_from_pc,
        )
        await bot.send_message(
            chat_id=chat_id,
            text=f"Узнай своё тотемное животное \n"
                 f"Пройди викторину от Московского Зоопарак \n"
                 f"Чтобы поучаствовать, нужно перейти по ссылке \n"
                 f"@MoskowZoo_bot",
        )
        await message.answer(
            'Ваш результат отправлен',
            reply_markup=btn_post()
        )
        await state.clear()
    except Exception as e:
        await message.answer(
            'Вы ввели неправильный ID',
            reply_markup=btn_step_end()
        )
        await state.clear()


@dp.message(F.text.in_(['Связаться с оператором']))
async def statement(message: types.Message):
    try:
        id = message.chat.id
        image_from_pc = FSInputFile(users[id]['image'])

        options = LinkPreviewOptions(url="https://t.me/Mikael_Anz")
        await message.answer(
            f"Приватный чат с сотрудником Зоопарка",
            link_preview_options=options,
            reply_markup=btn_statement()
        )
        await send_TechnicalChat(
            f"C вами хочет связаться пользователь { users[id]['name'] } \n "
                 f"Результат викторины"
        ),
        await send_TechnicalChat(
            users[id]['text']
        ),
        await message.bot.send_photo(
            chat_id=TechnicalChat,
            photo=image_from_pc,
        )
    except Exception as e:
        logger.log_error(f"Ошибка: {str(e)}")
        await send_TechnicalChat("Произошла ошибка в боте!")


@dp.message(F.text.in_(['Оставить отзыв!']))
async def comment(message: types.Message):
    btn = [
        [
            types.InlineKeyboardButton(text='плохо', callback_data='1'),
            types.InlineKeyboardButton(text='так себе', callback_data='2')
        ],
        [
            types.InlineKeyboardButton(text='хорошо', callback_data='3'),
            types.InlineKeyboardButton(text='отлично', callback_data='4')
        ],
    ]
    keyboard = types.InlineKeyboardMarkup(inline_keyboard=btn)
    await message.answer(
        "Оцените викторину!",
        reply_markup=keyboard
    )


@dp.callback_query(F.data.in_(['1', '2', '3', '4']))
async def comment_callback(callback: types.CallbackQuery):
    id = callback.message.chat.id
    if callback.data == '1':
        CreateReview(users[id]['name'], 'плохо', users[id]['text'])
    elif callback.data == '2':
        CreateReview(users[id]['name'], 'так себе', users[id]['text'])
    elif callback.data == '3':
        CreateReview(users[id]['name'], 'хорошо', users[id]['text'])
    elif callback.data == '4':
        CreateReview(users[id]['name'], 'отлично', users[id]['text'])

    await callback.message.delete()
    await callback.message.answer('Ваш отзыв принят!', reply_markup=btn_comment())


async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
