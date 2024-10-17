
from aiogram.types import (ReplyKeyboardMarkup, KeyboardButton,
                           InlineKeyboardButton, InlineKeyboardMarkup)
from aiogram.utils.keyboard import ReplyKeyboardBuilder, InlineKeyboardBuilder

check_man = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Посмотреть")]
],
    resize_keyboard=True,
)

choose_man = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="1"),
     KeyboardButton(text="2"),
     KeyboardButton(text="3"),
     KeyboardButton(text="4"),]
],
    resize_keyboard=True,
)

expert_video = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Посмотреть экспертное видео - почему мы выбираем именно таких мужчин")]
],
    resize_keyboard=True,
)

important_skill_before_relationships = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Далее")]
],
    resize_keyboard=True,
)

invitation_competition = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Далее")]
],
    resize_keyboard=True,
)

what_is_important_things_for_relationships = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Далее")]
],
    resize_keyboard=True,
)

things_for_relationship = ReplyKeyboardMarkup(keyboard=[
    [
        KeyboardButton(text="Самоценность"),
        KeyboardButton(text="Женственность"),
        KeyboardButton(text="Коммуникация"),
    ]
],
    resize_keyboard=True,
)

course = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Далее")]
],
    resize_keyboard=True,
)

first_lesson = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Получить первый урок бесплатно")]
],
    resize_keyboard=True,
)

payment = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Далее")]
],
    resize_keyboard=True,
    )