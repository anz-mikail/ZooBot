from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from answer import answer


def btn_welcome():
    btn = [KeyboardButton(text="Начать викторину")]
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Нажмите на кнопку",
        keyboard=[btn])
    return markup


def btn_start():
    btn = [
        KeyboardButton(text=answer['start'][1]),
        KeyboardButton(text=answer['start'][2])
    ]
    btn1 = [
        KeyboardButton(text=answer['start'][3]),
        KeyboardButton(text=answer['start'][4])
    ]
    btn2 = [
        KeyboardButton(text=answer['start'][5]),
        KeyboardButton(text=answer['start'][6])
    ]
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Нажмите на одну из кнопок",
        keyboard=[btn, btn1, btn2])
    return markup


def btn_ocean():
    btn = [KeyboardButton(text=answer['ocean'][1])]
    btn1 = [KeyboardButton(text=answer['ocean'][2])]
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Нажмите на одну из кнопок",
        keyboard=[btn, btn1])
    return markup


def btn_south():
    btn = [KeyboardButton(text=answer['south'][1])]
    btn1 = [KeyboardButton(text=answer['south'][2])]
    btn2 = [KeyboardButton(text=answer['south'][3])]
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Нажмите на одну из кнопок",
        keyboard=[btn, btn1, btn2])
    return markup


def btn_pre_herb():
    btn = [KeyboardButton(text=answer['pre_herb'][1])]
    btn1 = [KeyboardButton(text=answer['pre_herb'][2])]
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Нажмите на одну из кнопок",
        keyboard=[btn, btn1])
    return markup


def btn_wood():
    btn = [
        KeyboardButton(text=answer['wood'][1]),
        KeyboardButton(text=answer['wood'][2])
    ]
    btn1 = [
        KeyboardButton(text=answer['wood'][3]),
        KeyboardButton(text=answer['wood'][4])
    ]
    btn2 = [KeyboardButton(text=answer['wood'][5])]
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Нажмите на одну из кнопок",
        keyboard=[btn, btn1, btn2])
    return markup


def btn_plain_pre():
    btn = [KeyboardButton(text=answer['plain_pre'][1])]
    btn1 = [KeyboardButton(text=answer['plain_pre'][2])]
    btn2 = [KeyboardButton(text=answer['plain_pre'][3])]
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Нажмите на одну из кнопок",
        keyboard=[btn, btn1, btn2])
    return markup


def btn_plain_herb():
    btn = [
        KeyboardButton(text=answer['plain_herb'][1]),
        KeyboardButton(text=answer['plain_herb'][2])
    ]
    btn1 = [
        KeyboardButton(text=answer['plain_herb'][3]),
        KeyboardButton(text=answer['plain_herb'][4])
    ]
    btn2 = [
        KeyboardButton(text=answer['plain_herb'][5]),
        KeyboardButton(text=answer['plain_herb'][6])
    ]
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Нажмите на одну из кнопок",
        keyboard=[btn, btn1, btn2])
    return markup


def btn_birds():
    btn = [
        KeyboardButton(text=answer['birds'][1]),
        KeyboardButton(text=answer['birds'][2])
    ]
    btn1 = [
        KeyboardButton(text=answer['birds'][3]),
        KeyboardButton(text=answer['birds'][4])
    ]
    btn2 = [
        KeyboardButton(text=answer['birds'][5]),
        KeyboardButton(text=answer['birds'][6])
    ]
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Нажмите на одну из кнопок",
        keyboard=[btn, btn1, btn2])
    return markup


def btn_step1():
    btn = [
        KeyboardButton(text=answer['step_1'][1]),
        KeyboardButton(text=answer['step_1'][2])
    ]
    btn1 = [
        KeyboardButton(text=answer['step_1'][3]),
        KeyboardButton(text=answer['step_1'][4])
    ]
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Нажмите на одну из кнопок",
        keyboard=[btn, btn1])
    return markup


def btn_step2():
    btn = [
        KeyboardButton(text=answer['step_2'][1]),
        KeyboardButton(text=answer['step_2'][2])
    ]
    btn1 = [
        KeyboardButton(text=answer['step_2'][3]),
        KeyboardButton(text=answer['step_2'][4])
    ]
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Нажмите на одну из кнопок",
        keyboard=[btn, btn1])
    return markup


def btn_step3():
    btn = [
        KeyboardButton(text=answer['step_3'][1]),
        KeyboardButton(text=answer['step_3'][2])
    ]
    btn1 = [
        KeyboardButton(text=answer['step_3'][3]),
        KeyboardButton(text=answer['step_3'][4])
    ]
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Нажмите на одну из кнопок",
        keyboard=[btn, btn1])
    return markup


def btn_step4():
    btn = [
        KeyboardButton(text=answer['step_4'][1]),
        KeyboardButton(text=answer['step_4'][2])
    ]
    btn1 = [
        KeyboardButton(text=answer['step_4'][3]),
        KeyboardButton(text=answer['step_4'][4])
    ]
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Нажмите на одну из кнопок",
        keyboard=[btn, btn1])
    return markup


def btn_step5():
    btn = [
        KeyboardButton(text=answer['step_5'][1]),
        KeyboardButton(text=answer['step_5'][2])
    ]
    btn1 = [
        KeyboardButton(text=answer['step_5'][3]),
        KeyboardButton(text=answer['step_5'][4])
    ]
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Нажмите на одну из кнопок",
        keyboard=[btn, btn1])
    return markup


def btn_step6():
    btn = [
        KeyboardButton(text=answer['step_6'][1]),
        KeyboardButton(text=answer['step_6'][2])
    ]
    btn1 = [
        KeyboardButton(text=answer['step_6'][3]),
        KeyboardButton(text=answer['step_6'][4])
    ]
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Нажмите на одну из кнопок",
        keyboard=[btn, btn1])
    return markup


def btn_step7():
    btn = [
        KeyboardButton(text=answer['step_7'][1]),
        KeyboardButton(text=answer['step_7'][2])
    ]
    btn1 = [
        KeyboardButton(text=answer['step_7'][3]),
        KeyboardButton(text=answer['step_7'][4])
    ]
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Нажмите на одну из кнопок",
        keyboard=[btn, btn1])
    return markup


def btn_step8():
    btn = [
        KeyboardButton(text=answer['step_8'][1]),
        KeyboardButton(text=answer['step_8'][2])
    ]
    btn1 = [
        KeyboardButton(text=answer['step_8'][3]),
        KeyboardButton(text=answer['step_8'][4])
    ]
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Нажмите на одну из кнопок",
        keyboard=[btn, btn1])
    return markup


def btn_step9():
    btn = [
        KeyboardButton(text=answer['step_9'][1]),
        KeyboardButton(text=answer['step_9'][2])
    ]
    btn1 = [
        KeyboardButton(text=answer['step_9'][3]),
        KeyboardButton(text=answer['step_9'][4])
    ]
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Нажмите на одну из кнопок",
        keyboard=[btn, btn1])
    return markup


def btn_step10():
    btn = [
        KeyboardButton(text=answer['step_10'][1]),
        KeyboardButton(text=answer['step_10'][2])
    ]
    btn1 = [
        KeyboardButton(text=answer['step_10'][3]),
        KeyboardButton(text=answer['step_10'][4])
    ]
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Нажмите на одну из кнопок",
        keyboard=[btn, btn1])
    return markup


def btn_step_end():
    btn = [
        KeyboardButton(text='Повторить ещё'),
        KeyboardButton(text='Поделиться')
    ]
    btn1 = [
        KeyboardButton(text='Связаться с оператором'),
        KeyboardButton(text='Оставить отзыв!')
    ]
    markup = ReplyKeyboardMarkup(
        resize_keyboard=True,
        one_time_keyboard=True,
        input_field_placeholder="Выберите функцию!",
        keyboard=[btn, btn1])
    return markup

