from aiogram import Router, F, types

from Buttons import btn_step2, btn_step3, btn_step4, btn_step5, btn_step6, btn_step7, btn_step8, btn_step9, btn_step10
from answer import answer
from config import text_step_1, text_step_2, text_step_3, text_step_4, text_step_5, text_step_6, text_step_7, \
    text_step_8, text_step_9
from ..questions_path.path import users


router = Router()


@router.message(F.text.in_(text_step_1))
async def step_2(message: types.Message):
    id = message.chat.id
    if message.text == text_step_1[0]:
        users[id]['point'] += 5

    elif message.text == text_step_1[1]:
        users[id]['point'] += 10

    elif message.text == text_step_1[2]:
        users[id]['point'] += 15

    elif message.text == text_step_1[3]:
        users[id]['point'] += 20
    await message.answer(answer['step_2']['question'],
                         reply_markup=btn_step2())
    print('point', users)


@router.message(F.text.in_(text_step_2))
async def step_3(message: types.Message):
    id = message.chat.id
    if message.text == text_step_2[0]:
        users[id]['point'] += 5

    elif message.text == text_step_2[1]:
        users[id]['point'] += 10

    elif message.text == text_step_2[2]:
        users[id]['point'] += 15

    elif message.text == text_step_2[3]:
        users[id]['point'] += 20
    await message.answer(answer['step_3']['question'],
                         reply_markup=btn_step3())
    print('point', users)


@router.message(F.text.in_(text_step_3))
async def step_4(message: types.Message):
    id = message.chat.id
    if message.text == text_step_3[0]:
        users[id]['point'] += 5

    elif message.text == text_step_3[1]:
        users[id]['point'] += 10

    elif message.text == text_step_3[2]:
        users[id]['point'] += 15

    elif message.text == text_step_3[3]:
        users[id]['point'] += 20
    await message.answer(answer['step_4']['question'],
                         reply_markup=btn_step4())
    print('point', users)


@router.message(F.text.in_(text_step_4))
async def step_5(message: types.Message):
    id = message.chat.id
    if message.text == text_step_4[0]:
        users[id]['point'] += 5

    elif message.text == text_step_4[1]:
        users[id]['point'] += 10

    elif message.text == text_step_4[2]:
        users[id]['point'] += 15

    elif message.text == text_step_4[3]:
        users[id]['point'] += 20
    await message.answer(answer['step_5']['question'],
                         reply_markup=btn_step5())
    print('point', users)


@router.message(F.text.in_(text_step_5))
async def step_6(message: types.Message):
    id = message.chat.id
    if message.text == text_step_5[0]:
        users[id]['point'] += 5

    elif message.text == text_step_5[1]:
        users[id]['point'] += 10

    elif message.text == text_step_5[2]:
        users[id]['point'] += 15

    elif message.text == text_step_5[3]:
        users[id]['point'] += 20
    await message.answer(answer['step_6']['question'],
                         reply_markup=btn_step6())
    print('point', users)


@router.message(F.text.in_(text_step_6))
async def step_7(message: types.Message):
    id = message.chat.id
    if message.text == text_step_6[0]:
        users[id]['point'] += 5

    elif message.text == text_step_6[1]:
        users[id]['point'] += 10

    elif message.text == text_step_6[2]:
        users[id]['point'] += 15

    elif message.text == text_step_6[3]:
        users[id]['point'] += 20
    await message.answer(answer['step_7']['question'],
                         reply_markup=btn_step7())
    print('point', users)


@router.message(F.text.in_(text_step_7))
async def step_8(message: types.Message):
    id = message.chat.id
    if message.text == text_step_7[0]:
        users[id]['point'] += 5

    elif message.text == text_step_7[1]:
        users[id]['point'] += 10

    elif message.text == text_step_7[2]:
        users[id]['point'] += 15

    elif message.text == text_step_7[3]:
        users[id]['point'] += 20
    await message.answer(answer['step_8']['question'],
                         reply_markup=btn_step8())
    print('point', users)


@router.message(F.text.in_(text_step_8))
async def step_9(message: types.Message):
    id = message.chat.id
    if message.text == text_step_8[0]:
        users[id]['point'] += 5

    elif message.text == text_step_8[1]:
        users[id]['point'] += 10

    elif message.text == text_step_8[2]:
        users[id]['point'] += 15

    elif message.text == text_step_8[3]:
        users[id]['point'] += 20
    await message.answer(answer['step_9']['question'],
                         reply_markup=btn_step9())
    print('point', users)


@router.message(F.text.in_(text_step_9))
async def step_10(message: types.Message):
    id = message.chat.id
    if message.text == text_step_9[0]:
        users[id]['point'] += 5

    elif message.text == text_step_9[1]:
        users[id]['point'] += 10

    elif message.text == text_step_9[2]:
        users[id]['point'] += 15

    elif message.text == text_step_9[3]:
        users[id]['point'] += 20
    await message.answer(answer['step_10']['question'],
                         reply_markup=btn_step10())
    print('point', users)

