from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

socials = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Instagram"),
            KeyboardButton(text="YouTube")
        ],
        [
            KeyboardButton("TikTok"),
            KeyboardButton("Telegram")
        ]

    ],
    resize_keyboard=True
)

