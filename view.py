from keyboards.defaults.instagram import orqaqa
from keyboards.inlines.accses import view_button
from main import dp, bot, son, Shogirdchalar,  API_TOKEN
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from main import true_false, follow_button
from aiogram import types
from instagpy import InstaGPy



@dp.message_handler(state=Shogirdchalar.Instagram_state, text="Views 👁️")
async def views(message: Message, state: FSMContext):
    await message.answer("Stories yoki post linkini yuboring : ",reply_markup=orqaqa)
    await state.finish()
    await Shogirdchalar.views_state.set()



@dp.message_handler(state=Shogirdchalar.views_state, content_types=types.ContentType.TEXT)
async def views(message: Message, state: FSMContext):
    global url3
    url3 = message.text
    if url3.startswith("https://www.instagram.com"):
        photo = open('images/view.jpg', 'rb')
        await message.answer_photo(photo=photo, caption="Prasmotr sonini tanlang", reply_markup=view_button)
        await state.finish()
    else:
        await message.answer("Urlni noto'g'ri kiritdingiz qaytadan uriib ko'ring !")
        await Shogirdchalar.views_state.set()


@dp.callback_query_handler(text='view-')
async def minus_view(call: types.CallbackQuery, state: FSMContext):
    async def update_snecks_minus_view_button1(chat_id, message_id, new_son):
        view_button = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-1000 👁️', callback_data='view-'),
                    InlineKeyboardButton(text=f'{son[call.message.chat.id]}', callback_data='view_true'),
                    InlineKeyboardButton(text='+1000 👁️', callback_data='view+'),

                ],
                [
                    InlineKeyboardButton(text='Tasdiqlash✅', callback_data='view_tasdiqlash')
                ]
            ],
            resize_keyboard=True,
        )

        await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=view_button)

    global son
    print(True)
    if son[call.message.chat.id] <= 0:
        await call.answer('Eng kam miqdor 1000 ta')
    else:

        son[call.message.chat.id] -= 1000
        fake_son = son[call.message.chat.id]
        print(fake_son)
        if fake_son >= 0:
            await update_snecks_minus_view_button1(call.message.chat.id, call.message.message_id, fake_son)
        else:
            await call.answer('Eng kam miqdor 1000 ta')


@dp.callback_query_handler(text='view+')
async def plus_view(call: types.CallbackQuery):
    async def update_snecks_minus_view_button1(chat_id, message_id, new_son):
        view_button = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-1000 👁️', callback_data='view-'),
                    InlineKeyboardButton(text=f'{son[call.message.chat.id]}', callback_data='view_true'),
                    InlineKeyboardButton(text='+1000 👁️', callback_data='view+'),

                ],
                [
                    InlineKeyboardButton(text='Tasdiqlash✅', callback_data='view_tasdiqlash')
                ]
            ],
            resize_keyboard=True,
        )

        await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=view_button)

    global son
    son[call.message.chat.id] += 1000
    fake_son = son[call.message.chat.id]
    print(fake_son)
    if fake_son >= 0:
        await update_snecks_minus_view_button1(call.message.chat.id, call.message.message_id, fake_son)
    else:
        await call.answer('Eng kam miqdor 1000 ta')

@dp.callback_query_handler(text='view_tasdiqlash')
async def tasdiq_followers(call: types.CallbackQuery):
    await bot.send_message(6498877955,f'''
    <b>Yangi buyurtma</b>
Url : {url3}
Tur : <b>View</b>
Soni : <b>{son[call.message.chat.id]}</b>
Narxi : {son[call.message.chat.id] * 5} so'm
Username Telegrami : <a href="https://t.me/{call.message.chat.username}">@{call.message.chat.username}</a>
    ''',parse_mode="html")
    await call.message.answer(f'''
View soni : <b>{son[call.message.chat.id]}</b> 👁
Narxi : {son[call.message.chat.id] * 5} so'm 💰
To'lov karta raqami 💳 : <code>5614681909981023</code>

To'lovni qilgandan so'ng checkni adminga yuboring.
Yo'qsa buyurtmangiz amalga oshirilmaydi !

Admin : <a href="https://t.me/ra1mkulov_212">Admin Bot</a>
    ''')
