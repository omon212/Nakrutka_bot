from keyboards.defaults.instagram import orqaqa
from keyboards.inlines.accses import comment_button
from main import dp, bot, son, Shogirdchalar, API_TOKEN
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from main import true_false, follow_button
from aiogram import types
from instagpy import InstaGPy



@dp.message_handler(state=Shogirdchalar.Instagram_state, text="Comments 💬")
async def comments(message: Message, state: FSMContext):
    await message.answer("Stories yoki post linkini yuboring : ",reply_markup=orqaqa)
    await state.finish()
    await Shogirdchalar.comment_state.set()


@dp.message_handler(state=Shogirdchalar.comment_state, content_types=types.ContentType.TEXT)
async def comments(message: Message, state: FSMContext):
    global url2
    url2 = message.text
    if url2.startswith("https://www.instagram.com"):
        photo = open('images/comment.png', 'rb')
        await message.answer_photo(photo=photo, caption="Kamentariya sonini tanlang", reply_markup=comment_button)
        await state.finish()
    else:
        await message.answer("Urlni noto'g'ri kiritdingiz qaytadan uriib ko'ring !")
        await Shogirdchalar.comment_state.set()


@dp.callback_query_handler(text='comment-')
async def minus_comment(call: types.CallbackQuery, state: FSMContext):
    async def update_snecks_minus_comment_button1(chat_id, message_id, new_son):
        comment_button = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-1000 💬', callback_data='comment-'),
                    InlineKeyboardButton(text=f'{son[call.message.chat.id]}', callback_data='comment_true'),
                    InlineKeyboardButton(text='+1000 💬', callback_data='comment+'),

                ],
                [
                    InlineKeyboardButton(text='Tasdiqlash✅', callback_data='comment_tasdiqlash')
                ]
            ],
            resize_keyboard=True,
        )

        await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=comment_button)

    global son
    print(True)
    if son[call.message.chat.id] <= 0:
        await call.answer('Eng kam miqdor 1000 ta')
    else:

        son[call.message.chat.id] -= 1000
        fake_son = son[call.message.chat.id]
        print(fake_son)
        if fake_son >= 0:
            await update_snecks_minus_comment_button1(call.message.chat.id, call.message.message_id, fake_son)
        else:
            await call.answer('Eng kam miqdor 1000 ta')

#
@dp.callback_query_handler(text='comment+')
async def plus_comment(call: types.CallbackQuery):
    async def update_snecks_minus_comment_button1(chat_id, message_id, new_son):
        comment_button = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-1000 💬', callback_data='comment-'),
                    InlineKeyboardButton(text=f'{son[call.message.chat.id]}', callback_data='comment_true'),
                    InlineKeyboardButton(text='+1000 💬', callback_data='comment+'),

                ],
                [
                    InlineKeyboardButton(text='Tasdiqlash✅', callback_data='comment_tasdiqlash')
                ]
            ],
            resize_keyboard=True,
        )

        await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=comment_button)

    global son
    son[call.message.chat.id] += 1000
    fake_son = son[call.message.chat.id]
    print(fake_son)
    if fake_son >= 0:
        await update_snecks_minus_comment_button1(call.message.chat.id, call.message.message_id, fake_son)
    else:
        await call.answer('Eng kam miqdor 1000 ta')

@dp.callback_query_handler(text='comment_tasdiqlash')
async def tasdiq_followers(call: types.CallbackQuery):
    await bot.send_message(6498877955,f'''
    <b>Yangi buyurtma</b>
Url : {url2}
Tur : <b>Comment</b>
Soni : <b>{son[call.message.chat.id]}</b>
Narxi : {son[call.message.chat.id] * 5} so'm
Username Telegrami : <a href="https://t.me/{call.message.chat.username}">@{call.message.chat.username}</a>
    ''',parse_mode="html")
    await call.message.answer(f'''
Commentlar soni : <b>{son[call.message.chat.id]}</b> 💬
Narxi : {son[call.message.chat.id] * 5} so'm 💰
To'lov karta raqami 💳 : <code>8600092990835856</code>

To'lovni qilgandan so'ng checkni adminga yuboring.
Yo'qsa buyurtmangiz amalga oshirilmaydi !

Admin : <a href="https://t.me/check_nakrutka">ADMIN CHECK BOT</a>
    ''')