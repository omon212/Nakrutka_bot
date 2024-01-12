from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton


true_false = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Ha✅",callback_data="ha"),
            InlineKeyboardButton(text="Yoq❌",callback_data="yoq")
        ]
    ]
)
follow_button = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                InlineKeyboardButton('-1000👤', callback_data='minus_follow'),
                InlineKeyboardButton(f'0', callback_data='0'),
                InlineKeyboardButton('+1000👤', callback_data='plus_follow')
            ],
            [
                InlineKeyboardButton('Tasdiqlash✅', callback_data='follow_tasdiqlash')
            ]
        ])

like_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='-1000 ❤️', callback_data='like-'),
            InlineKeyboardButton(text=f'0', callback_data='like_true'),

            InlineKeyboardButton(text='+1000 ❤️', callback_data='like+'),

        ],
        [
            InlineKeyboardButton(text='Tasdiqlash✅', callback_data='like_tasdiqlash')
        ]
    ],
    resize_keyboard=True,
)


view_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='-1000 👁️', callback_data='view-'),
            InlineKeyboardButton(text=f'0', callback_data='view_true'),

            InlineKeyboardButton(text='+1000 👁️', callback_data='view+'),

        ],
        [
            InlineKeyboardButton(text='Tasdiqlash✅', callback_data='view_tasdiqlash')
        ]
    ],
    resize_keyboard=True,
)


comment_button = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='-1000 💬', callback_data='comment-'),
            InlineKeyboardButton(text=f'0', callback_data='comment_true'),

            InlineKeyboardButton(text='+1000 💬', callback_data='comment+'),

        ],
        [
            InlineKeyboardButton(text='Tasdiqlash✅', callback_data='comment_tasdiqlash')
        ]
    ],
    resize_keyboard=True,
)