from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton

til = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='πΊπΏ uz',callback_data='uz'),
            InlineKeyboardButton(text='πΊπΈ eng',callback_data='en'),
            InlineKeyboardButton(text='π·πΊ ru',callback_data='ru')
        ],
    ]
)


rek = InlineKeyboardMarkup(
    inline_keyboard=[
    [
        InlineKeyboardButton(text='β Ha',callback_data='ha'),
        InlineKeyboardButton(text="β Yo'q",callback_data="yuq")
    ],
    ]
)