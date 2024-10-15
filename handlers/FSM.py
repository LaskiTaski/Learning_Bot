from aiogram.dispatcher.filters.state import State, StatesGroup
from bot_telegram import bot
from aiogram import Dispatcher
from keyboards.kb_FSM import *


class FSMClient(StatesGroup):
    start = State()
    video = State()
    homework = State()
    project = State()
    learn = State()
    book = State()


# @dp.message_handler(commands=['start'], state='*')
async def cmd_start(message: types.Message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(Video, HomeWork, Learn, Book)
    await FSMClient.start.set()
    await bot.send_message(chat_id=message.from_user.id,
                           text='Выберите раздел',
                           reply_markup=kb)


# @dp.callback_query_handlers(text='Menu', state='*')
async def cb_menu(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(Video, HomeWork, Learn, Book)
    await FSMClient.start.set()
    await callback.message.edit_text('Выберите раздел', reply_markup=kb)


# @dp.callback_query_handlers(text='Video', state=(FSMClient.start, None))
async def cb_video(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(Module1, Module2, Module3, Module4, AllMenu)
    await FSMClient.video.set()
    await callback.message.edit_text('Видеоматериалы по:', reply_markup=kb)


# @dp.callback_query_handlers(text='HomeWork', state=(FSMClient.start, None))
async def cb_homework(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=1)
    kb.add(Module1, Module2, Module3, Module4, AllMenu)
    await FSMClient.homework.set()
    await callback.message.edit_text('Домашнее задание по:', reply_markup=kb)


# @dp.callback_query_handlers(text='Project', state=(FSMClient.start, None))
# async def cb_project(callback: types.CallbackQuery):
#     kb = types.InlineKeyboardMarkup(row_width=1)
#     kb.add(Module1, Module2, Module3, AllMenu)
#     await FSMClient.project.set()
#     await callback.message.edit_text('Проекты по:', reply_markup=kb)


# @dp.callback_query_handlers(text='Learn', state=(FSMClient.start, None))
async def cb_learn(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=3)
    kb.add(*gen_learn_button(callback.data))
    kb.row(AllMenu)
    await FSMClient.learn.set()
    info = gen_learn_info()[callback.data]
    await callback.message.edit_text(f"[{info[0]}]"
                                     f"({info[1]})",
                                     reply_markup=kb)


# @dp.callback_query_handlers(text='Book', state=(FSMClient.start, None))
async def cb_book(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=3)
    kb.add(*gen_book_button(callback.data))
    kb.row(AllMenu)

    await FSMClient.book.set()
    info = gen_book_info()[callback.data]
    await callback.message.edit_text(f"[{info[0]}]"
                                     f"({info[1]})",
                                     reply_markup=kb)


def register_handlers_machine(dp: Dispatcher):
    dp.register_message_handler(cmd_start, commands=['start'], state='*')
    dp.register_callback_query_handler(cb_menu, text='Menu', state='*')
    dp.register_callback_query_handler(cb_video, text='Video', state=(FSMClient.start, None))
    dp.register_callback_query_handler(cb_homework, text='HomeWork', state=(FSMClient.start, None))
    # dp.register_callback_query_handler(cb_project, text='Project', state=(FSMClient.start, None))

    dp.register_callback_query_handler(cb_learn, text=('Learn', 'lvl2', 'lvl3', 'lvl4', 'lvl5', 'lvl6', 'lvl7'),
                                       state=(FSMClient.start, FSMClient.learn, None))

    dp.register_callback_query_handler(cb_book, text=('Book', 'str', 'list', 'dict', 'open', 'turtle', 'OOP'),
                                       state=(FSMClient.start, FSMClient.book, None))
