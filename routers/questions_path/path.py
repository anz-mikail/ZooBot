from aiogram import Router, F, types

from Buttons import btn_start, btn_ocean, btn_south, btn_pre_herb, btn_wood, btn_plain_pre, btn_step1, btn_plain_herb, \
    btn_birds
from answer import answer
from config import text_ocean, text_south, text_pre_herb, text_predatory, text_herbivores, text_birds, text_step_birds,\
    text_step_south_bats, text_step_wood, text_step_plain, text_start


router = Router()

users = {}


@router.message(F.text.in_(text_start))
async def start(message: types.Message):
    global rezult
    user = message.from_user
    id = message.chat.id
    users[id] = {}
    users[id]['name'] = user.full_name
    users[id]['code'] = ['a', 'a']
    users[id]['point'] = 0
    rezult = users[id]['code']
    await message.answer(answer['start']['question'],
                         reply_markup=btn_start())
    print(users)


@router.message(F.text.in_(text_ocean))
async def ocean(message: types.Message):
    global rezult
    rezult.clear()
    rezult.append('ocean')
    await message.answer(answer['ocean']['question'],
                         reply_markup=btn_ocean())
    print(users)


@router.message(F.text.in_(text_south))
async def south(message: types.Message):
    global rezult
    rezult.append('south')
    await message.answer(answer['south']['question'],
                         reply_markup=btn_south())
    print(users)


@router.message(F.text.in_(text_pre_herb))
async def pre_herb(message: types.Message):
    global rezult
    if message.text == text_pre_herb[0]:
        rezult.clear()
        rezult.append('swamp')

    elif message.text == text_pre_herb[1]:
        rezult.clear()
        rezult.append('wood_jungles')

    elif message.text == text_pre_herb[2]:
        rezult.clear()
        rezult.append('plain_dune')

    elif message.text == text_pre_herb[3]:
        rezult.clear()
        rezult.append('mount')

    elif rezult[0] == 'ocean':
        rezult.append('nord')
    await message.answer(answer['pre_herb']['question'],
                         reply_markup=btn_pre_herb()),
    print(users)


@router.message(F.text.in_(text_predatory))
async def predatory(message: types.Message):
    global rezult
    rezult.append('predatory')
    if rezult[0] == 'wood_jungles':
        await message.answer(answer['wood']['question'], reply_markup=btn_wood())

    elif rezult[0] == 'plain_dune':
        await message.answer(answer['plain_pre']['question'], reply_markup=btn_plain_pre())

    elif rezult[0] == 'mount':
        await message.answer(answer['plain_pre']['question'], reply_markup=btn_plain_pre())

    else:
        await message.answer(answer['step_1']['question'], reply_markup=btn_step1())
    print(users)


@router.message(F.text.in_(text_herbivores))
async def herbivores(message: types.Message):
    global rezult
    rezult.append('herbivores')
    if rezult[0] == 'wood_jungles':
        await message.answer(answer['wood']['question'], reply_markup=btn_wood())

    elif rezult[0] == 'plain_dune':
        await message.answer(answer['plain_herb']['question'], reply_markup=btn_plain_herb())

    else:
        await message.answer(answer['step_1']['question'], reply_markup=btn_step1())
    print(users)


@router.message(F.text.in_(text_birds))
async def birds(message: types.Message):
    global rezult
    rezult.append('birds')
    await message.answer(answer['birds']['question'],
                         reply_markup=btn_birds())
    print(users)


@router.message(F.text.in_(text_step_birds))
async def step_birds(message: types.Message):
    global rezult
    if message.text == text_step_birds[0]:
        rezult.append('cancerous')

    elif message.text == text_step_birds[1]:
        rezult.append('chicken')

    elif message.text == text_step_birds[2]:
        rezult.append('crane')

    elif message.text == text_step_birds[3]:
        rezult.append('goose')

    elif message.text == text_step_birds[4]:
        rezult.append('pigeon')

    elif message.text == text_step_birds[5]:
        rezult.append('turaco')
    await message.answer(answer['step_1']['question'],
                         reply_markup=btn_step1())
    print(users)


@router.message(F.text.in_(text_step_south_bats))
async def south_bats(message: types.Message):
    global rezult
    if message.text == text_step_south_bats[0]:
        rezult.clear()
        rezult.append('bats')

    elif message.text == text_step_south_bats[1]:
        rezult.append('turtle')

    elif message.text == text_step_south_bats[2]:
        rezult.append('flamingo')

    elif message.text == text_step_south_bats[3]:
        rezult.append('stork')
    await message.answer(answer['step_1']['question'],
                         reply_markup=btn_step1())
    print(users)


@router.message(F.text.in_(text_step_wood))
async def step_woods(message: types.Message):
    global rezult
    if rezult[1] == 'predatory':
        if message.text == text_step_wood[0]:
            rezult.append('cats')
        elif message.text == text_step_wood[1]:
            rezult.append('scaly')
        elif message.text == text_step_wood[2]:
            rezult.append('dogs')
        elif message.text == text_step_wood[3]:
            rezult.append('raccoon')
        elif message.text == text_step_wood[4]:
            rezult.append('owl')

    elif rezult[1] == 'herbivores':
        if message.text == text_step_wood[0]:
            rezult.append('parrot')
        elif message.text == text_step_wood[1]:
            rezult.append('artiodactyls')
        elif message.text == text_step_wood[2]:
            rezult.append('primates')
        elif message.text == text_step_wood[3]:
            rezult.append('rodents')
        elif message.text == text_step_wood[4]:
            rezult.append('sparrow')
    await message.answer(answer['step_1']['question'],
                         reply_markup=btn_step1())
    print(users)


@router.message(F.text.in_(text_step_plain))
async def step_1(message: types.Message):
    global rezult
    if rezult[1] == 'predatory':
        if message.text == text_step_plain[0]:
            rezult.append('cats')
        elif message.text == text_step_plain[1]:
            rezult.append('falcon')
        elif message.text == text_step_plain[2]:
            rezult.append('dogs')

    elif rezult[1] == 'herbivores':
        if message.text == text_step_plain[3]:
            rezult.append('incomplete_teeth')
        elif message.text == text_step_plain[4]:
            rezult.append('rodents')
        elif message.text == text_step_plain[5]:
            rezult.append('marsupials')
        elif message.text == text_step_plain[6]:
            rezult.append('ungulates')
        elif message.text == text_step_plain[7]:
            rezult.append('artiodactyls')
    await message.answer(answer['step_1']['question'],
                         reply_markup=btn_step1())
    print(users)
