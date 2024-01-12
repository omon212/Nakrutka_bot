from aiogram.types import ReplyKeyboardMarkup,KeyboardButton


instagram_paket = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Followers 👤"),
            KeyboardButton(text="Likes ❤️")
        ],
        [
            KeyboardButton(text="Views 👁️"),
            KeyboardButton(text="Comments 💬")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

orqaqa = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Asosiy menu🔙")
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)