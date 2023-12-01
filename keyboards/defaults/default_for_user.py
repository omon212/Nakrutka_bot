from aiogram.types import KeyboardButton, ReplyKeyboardMarkup

socials = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Instagram"),
            KeyboardButton(text="YouTube")
        ],
        [
            KeyboardButton(text="TikTok"),
            KeyboardButton(text="Telegram")
        ]

    ],
    resize_keyboard=True
)

