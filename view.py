from main import dp, bot, son, Shogirdchalar, user_instagram, API_TOKEN
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.dispatcher import FSMContext
from main import true_false, follow_button
from aiogram import types
from instagpy import InstaGPy




@dp.message_handler(state=Shogirdchalar.Instagram_state, text="Views👁️")
async def views(message: Message, state: FSMContext):
    await message.answer("Url kiriting")
    await state.finish()
    await Shogirdchalar.views_state.set()



@dp.message_handler(state=Shogirdchalar.views_state, content_types=types.ContentType.TEXT)
async def views(message: Message, state: FSMContext):
    url = message.text
    user_instagram[str(message.from_user.id)] = url
    if url.startswith("https://www.instagram.com"):
        link = "https://yt3.googleusercontent.com/VJAWgMbfJ-umoqgiPIh8Zq2R1ZUm2IuGaT75GBY0OHFLrk0nKhR-pt8DrNotRAjk49Qhor0t=s900-c-k-c0x00ffffff-no-rj"
        await message.answer_photo(link, caption="Prasmotr sonini tanlang", reply_markup=view_button)
        await state.finish()
    else:
        await message.answer("Tentak")


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
async def tasdiq_view(call: types.CallbackQuery):
    instagram_nomi = user_instagram[f"{call.message.chat.id}"]
    await bot.send_message(6596589901,
                           f"Yangi Zakaz keldi\nBuyurtmachi: {call.from_user.username}\nTanlov Turi: View\nSoni: {son[call.message.chat.id]}\nInstagram: {instagram_nomi}")
    await call.message.answer("To`lov turini tanlang!")