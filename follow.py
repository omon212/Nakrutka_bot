from main import dp, bot, son, Shogirdchalar, user_instagram, API_TOKEN
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from main import true_false, follow_button
from aiogram import types
from instagpy import InstaGPy

@dp.message_handler(state=Shogirdchalar.Instagram_state, text="Followers👤")
async def followers(message: Message, state: FSMContext):
    await message.answer("Username Kiriting")
    await state.finish()
    await Shogirdchalar.username_insta_state.set()


@dp.message_handler(state=Shogirdchalar.username_insta_state)
async def username(message: Message, state: FSMContext):
    user = message.text
    insta = InstaGPy(use_mutiple_account=False, session_ids=None, min_requests=None, max_requests=None)
    txt = insta.get_user_basic_details(f'{user}')
    print(txt)
    user_instagram[f'{message.from_user.id}'] = txt["username"]
    await message.answer(f"""
Username: {txt["username"]}

Full Name : {txt["full_name"]}

Private : {txt["is_private"]}


<b>Sizning akkauntingizligiga ishonchingiz komilmi?</b>
    """, reply_markup=true_false)


# -----------------------FOLLOW_________________________________________________________


@dp.callback_query_handler(text='ha', state=Shogirdchalar.username_insta_state)
async def followers(call: types.CallbackQuery, state: FSMContext):
    await call.message.delete()
    photo = 'https://img.freepik.com/premium-vector/100k-social-media-followers-design_54625-114.jpg?w=2000'
    await call.message.answer_photo(photo, reply_markup=follow_button, caption="Follow👥")
    await state.finish()


@dp.callback_query_handler(text='plus_follow')
async def plus_follow(call: types.CallbackQuery):
    global son
    son[call.message.chat.id] += 1000
    fake_son = son[call.message.chat.id]
    print(fake_son)
    if fake_son >= 0:
        await update_snecks_follow_button(call.message.chat.id, call.message.message_id, fake_son)
    else:
        await call.answer('Eng kam miqdor 1000 ta')


async def update_snecks_follow_button(chat_id, message_id, new_son):
    follow_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('-1000👤', callback_data='minus_follow'),
                InlineKeyboardButton(f'{new_son}', callback_data='0'),
                InlineKeyboardButton('+1000👤', callback_data='plus_follow')
            ],
            [
                InlineKeyboardButton('Tasdiqlash✅', callback_data='follow_tasdiqlash')
            ]
        ])

    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=follow_button)


@dp.callback_query_handler(text='minus_follow')
async def minus_follow(call: types.CallbackQuery, state: FSMContext):
    global son
    print(True)
    if son[call.message.chat.id] <= 0:
        await call.answer('Eng kam miqdor 1000 ta')
    else:
        son[call.message.chat.id] -= 1000
        fake_son = son[call.message.chat.id]
        print(fake_son)
        if fake_son >= 0:
            await update_snecks_minus_follow_button1(call.message.chat.id, call.message.message_id, fake_son)
        else:
            await call.answer('Eng kam miqdor 1000 ta')


async def update_snecks_minus_follow_button1(chat_id, message_id, new_son):
    minus_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('-1000👤', callback_data='minus_follow'),
                InlineKeyboardButton(f'{new_son}', callback_data='0'),
                InlineKeyboardButton('+1000👤', callback_data='plus_follow')
            ],
            [
                InlineKeyboardButton('Tasdiqlash✅', callback_data='follow_tasdiqlash')
            ]
        ])

    await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=minus_button)


@dp.callback_query_handler(text='follow_tasdiqlash')
async def tasdiq_followers(call: types.CallbackQuery):
    instagram_nomi = user_instagram[f"{call.message.chat.id}"]
    await bot.send_message(
        6498877955,
        f"<b>Yangi Zakaz keldi</b>\n<b>Buyurtmachi</b>: {call.from_user.username}\n<b>Tanlov Turi</b>: Obunachi\n<b>Soni</b>: {son[call.message.chat.id]}\n<b>Instagram</b>: <a href='https://instagram.com/{instagram_nomi}'>{instagram_nomi}</a>",
        parse_mode="html"
    )
    await call.message.answer("Tolov turini tanlang : ")
