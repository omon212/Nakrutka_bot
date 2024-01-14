import logging
from aiogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.utils import executor
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from keyboards.defaults.instagram import instagram_paket, orqaqa, phone
from instagpy import InstaGPy
import sqlite3


logging.basicConfig(level=logging.INFO)
from keyboards.inlines.accses import true_false, follow_button, like_button, view_button, comment_button

API_TOKEN = '6014525433:AAG580QB5WriakLaLxcPjT4sRIUgW-F86bs'

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
    views_state = State()
    comment_state = State()
    get_phone = State()



conn = sqlite3.connect('stats.db')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS stats
                  (id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user_id INTEGER,
                   date DATE)''')

conn.commit()


def record_stat(user_id):
    cursor.execute("INSERT INTO stats (user_id, date) VALUES (?, DATE('now'))", (user_id,))
    conn.commit()





@dp.message_handler(commands=['stats'])
async def show_stats(message: types.Message):
    cursor.execute("SELECT COUNT(DISTINCT user_id) FROM stats")
    total_users = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(DISTINCT user_id) FROM stats WHERE date = DATE('now')")
    today_users = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM stats")
    total_requests = cursor.fetchone()[0]
    cursor.execute("SELECT COUNT(*) FROM stats WHERE date = DATE('now')")
    today_requests = cursor.fetchone()[0]
    text = f"📊 Botdan foydalanish statistikasi:\n" \
           f" ├ Jami foydalanuvchilar: {total_users}\n" \
           f" ├ Bugungi foydalanuvchilar: {today_users}\n" \
           f" ├ Jami so'rovlar: {total_requests}\n" \
           f" └ Bugungi so'rovlar: {today_requests}"
    await message.reply(text)





@dp.message_handler(commands=['start','help'])
async def start(message:Message):
    await message.answer("<b>I N S T A G R A M</b> botiga xush kelibsiz! ")
    await message.answer('''
Avval telefon raqamingizni yuboring,
yoki <b>+998XX XXXXXXX</b> ko'rinishida yozing.    
    ''',reply_markup=phone)
    await Shogirdchalar.get_phone.set()

@dp.message_handler(content_types=types.ContentType.CONTACT,state=Shogirdchalar.get_phone)
async def for_start(message: types.Message, state: FSMContext):

    son[message.from_user.id] = 0
    await message.answer(f"""
Bizning Instagram uchun Nakrutka botiga xuch kelibsiz

Sizga qaysi xizmat kerak bolsa, quyida xizmatlardan birini tanlang!
    """, reply_markup=instagram_paket)
    await state.finish()
    await Shogirdchalar.Instagram_state.set()


@dp.message_handler(state=Shogirdchalar.Instagram_state, text="Likes ❤️")
async def likes(message: Message, state: FSMContext):
    await message.answer("Stories yoki post linkini yuboring : ",reply_markup=orqaqa)
    await state.finish()
    await Shogirdchalar.url_like_state.set()


@dp.message_handler(state=Shogirdchalar.url_like_state, content_types=types.ContentType.TEXT)
async def likes(message: Message, state: FSMContext):
    global url
    url = message.text

    if url.startswith("https://www.instagram.com"):
        link = open('images/like.png', 'rb')
        await message.answer_photo(link, caption="Like sonini tanlang", reply_markup=like_button)
        await state.finish()
    else:
        await message.answer("Url noto'gri kiritildi qaytadan urinib koring !",reply_markup=orqaqa)
        await Shogirdchalar.url_like_state.set()


# gi
@dp.callback_query_handler(text='like-')
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
                    InlineKeyboardButton(text='Tasdiqlash✅', callback_data='like_tasdiqlash')
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


@dp.callback_query_handler(text='like+')
async def plus_like(call: types.CallbackQuery):
    async def update_snecks_minus_like_button1(chat_id, message_id, new_son):
        like_button = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(text='-1000 ❤️', callback_data='like-'),
                    InlineKeyboardButton(text=f'{son[call.message.chat.id]}', callback_data='like_true'),
                    InlineKeyboardButton(text='+1000 ❤️', callback_data='like+'),

                ],
                [
                    InlineKeyboardButton(text='Tasdiqlash✅', callback_data='like_tasdiqlash')
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
















@dp.callback_query_handler(text='like_tasdiqlash')
async def tasdiq_followers(call: types.CallbackQuery):
    await bot.send_message(6498877955,f'''
    <b>Yangi buyurtma</b>
Url : {url}
Tur : <b>Like</b>
Soni : <b>{son[call.message.chat.id]}</b>
Narxi : {son[call.message.chat.id] * 5} so'm
Username Telegrami : <a href="https://t.me/{call.message.chat.username}">@{call.message.chat.username}</a>
    ''',parse_mode="html")
    await call.message.answer(f'''
Likelar soni : <b>{son[call.message.chat.id]}</b> ❤️
Narxi : {son[call.message.chat.id] * 5} so'm 💰
To'lov karta raqami 💳 : <code>8600092990835856</code>

To'lovni qilgandan so'ng checkni adminga yuboring.
Yo'qsa buyurtmangiz amalga oshirilmaydi !

Admin : <a href="https://t.me/check_nakrutka">ADMIN CHECK BOT</a>
    ''')
@dp.message_handler(text="Asosiy menu🔙")
async def orqaga_qaytish(message: types.Message,state:FSMContext):
    await message.answer("Tanlang : ", reply_markup=instagram_paket)
    await Shogirdchalar.Instagram_state.set()

if __name__ == '__main__':
    from follow import dp,bot
    from view import dp,bot
    from comment import dp,bot
    executor.start_polling(dp, skip_updates=True)
