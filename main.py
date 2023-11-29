import logging
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from keyboards.defaults.default_for_user import socials
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboards.defaults.instagram import instagram_paket
from instagpy import InstaGPy

# Set up logging
logging.basicConfig(level=logging.INFO)
from keyboards.inlines.accses import true_false, follow_button, like_button

API_TOKEN = '6762535664:AAE2siFE6bDMGFvRqph9MUFmO1qIAWR2rVY'

bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())

son = {
    "user_id": 0
}


class Shogirdchalar(StatesGroup):
    Socials_button_state = State()
    Instagram_state = State()
    YouTube_state = State()
    TikTok_state = State()
    Telegram_state = State()
    username_insta_state = State()
    url_like_state = State()


@dp.message_handler(commands='start')
async def for_start(message: types.Message, state: FSMContext):
    son[message.from_user.id] = 0
    await message.answer(message.from_user.id)
    await message.answer(f"Assalomu Aleykum <code>{message.from_user.full_name}</code>", reply_markup=socials)
    await Shogirdchalar.Socials_button_state.set()


@dp.message_handler(text="Instagram", state=Shogirdchalar.Socials_button_state)
async def insta_logging(message: Message, state: FSMContext):
    await message.answer("Siz Instagram Bo`limini Tanladingiz\n\nTariflardan birini tanlang",
                         reply_markup=instagram_paket)
    await state.finish()
    await Shogirdchalar.Instagram_state.set()


@dp.message_handler(state=Shogirdchalar.Instagram_state, text="Followers")
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


# _____________________________________FOWLLOW_END_____________________________
#--------------------------------------LIKE-----------------------------------

@dp.message_handler(state=Shogirdchalar.Instagram_state, text="Likes")
async def followers(message: Message, state: FSMContext):
    await message.answer("Url kiriting")
    await state.finish()
    await Shogirdchalar.url_like_state.set()


@dp.message_handler(state=Shogirdchalar.url_like_state, content_types=types.ContentType.TEXT)
async def followers(message: Message, state: FSMContext):
    url = message.text
    if url.startswith("https://www.instagram.com"):
        link = "https://avatars.mds.yandex.net/i?id=a21ba0b3957dd0573d399a4891039d13207de203-10139706-images-thumbs&n=13"
        await message.answer_photo(link,caption = "Like tanlang",reply_markup=like_button)
        await state.finish()

    else:
        await message.answer("Tentak")
@dp.callback_query_handler(text = 'like-')
async def minus_like(call: types.CallbackQuery, state: FSMContext):
    async def update_snecks_minus_like_button1(chat_id, message_id, new_son):
        like_button = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-1000 ❤️', callback_data='like-'),
                    InlineKeyboardButton(text=f'{son[call.message.chat.id]}', callback_data='like_true'),
                    InlineKeyboardButton(text='+1000 ❤️', callback_data='like+'),

                ],
                [
                    InlineKeyboardButton(text='Tasdiqlash', callback_data='Tasdiqlash_like')
                ]
            ],
            resize_keyboard=True,
        )

        await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=like_button)
    global son
    print(True)
    if son[call.message.chat.id] <= 0:
        await call.answer('Eng kam miqdor 1000 ta')
    else:

        son[call.message.chat.id] -= 1000
        fake_son = son[call.message.chat.id]
        print(fake_son)
        if fake_son >= 0:
            await update_snecks_minus_like_button1(call.message.chat.id, call.message.message_id, fake_son)
        else:
            await call.answer('Eng kam miqdor 1000 ta')
@dp.callback_query_handler(text = 'like+')
async def plus_follow(call: types.CallbackQuery):
    async def update_snecks_minus_like_button1(chat_id, message_id, new_son):
        like_button = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-1000 ❤️', callback_data='like-'),
                    InlineKeyboardButton(text=f'{son[call.message.chat.id]}', callback_data='like_true'),
                    InlineKeyboardButton(text='+1000 ❤️', callback_data='like+'),

                ],
                [
                    InlineKeyboardButton(text='Tasdiqlash', callback_data='Tasdiqlash_like')
                ]
            ],
            resize_keyboard=True,
        )

        await bot.edit_message_reply_markup(chat_id=chat_id, message_id=message_id, reply_markup=like_button)
    global son
    son[call.message.chat.id] += 1000
    fake_son = son[call.message.chat.id]
    print(fake_son)
    if fake_son >= 0:
        await update_snecks_minus_like_button1(call.message.chat.id, call.message.message_id, fake_son)
    else:
        await call.answer('Eng kam miqdor 1000 ta')

#-------------------------LIKE_end-------------------------------------



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
