import logging
from aiogram.types import Message
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

API_TOKEN = '6762535664:AAE2siFE6bDMGFvRqph9MUFmO1qIAWR2rVY'

bot = Bot(token=API_TOKEN, parse_mode="HTML")
dp = Dispatcher(bot, storage=MemoryStorage())


class Shogirdchalar(StatesGroup):
    Socials_button_state = State()
    Instagram_state = State()
    YouTube_state = State()
    TikTok_state = State()
    Telegram_state = State()
    username_insta_state = State()


@dp.message_handler(commands='start')
async def for_start(message: types.Message,state: FSMContext):
    await message.answer(f"Assalomu Aleykum <code>{message.from_user.full_name}</code>", reply_markup=socials)
    await Shogirdchalar.Socials_button_state.set()

@dp.message_handler(text = "Instagram",state=Shogirdchalar.Socials_button_state)
async def insta_logging(message: Message, state:FSMContext):
    await message.answer("Siz Instagram Bo`limini Tanladingiz\n\nTariflardan birini tanlang",reply_markup=instagram_paket)
    await state.finish()
    await Shogirdchalar.Instagram_state.set()


@dp.message_handler(state=Shogirdchalar.Instagram_state,text = "Followers")
async def followers(message: Message,state:FSMContext):
    await message.answer("Username Kiriting")
    await state.finish()
    await Shogirdchalar.username_insta_state.set()
@dp.message_handler(state=Shogirdchalar.username_insta_state)
async def username(message:Message,state:FSMContext):
    user = message.text
    insta = InstaGPy(use_mutiple_account=False, session_ids=None, min_requests=None, max_requests=None)
    txt = insta.get_user_basic_details(f'{user}')
    print(txt)
    await message.answer(f"""
Username: {txt["username"]}
Full Name : {txt["full_name"]}
Private : {txt["is_private"]}
    """)




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

