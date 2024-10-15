from aiogram import Dispatcher, types
from keyboards.kb_HomeWork import *
from handlers.FSM import FSMClient
from keyboards.kb_FSM import AllMenu


# @dp.callback_query_handlers(lambda x: x.data in gen_video_info()[0], state=(FSMClient.video, None))
async def cb_homework_module1(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=3)
    kb.add(*gen_homework_button(callback.data))
    kb.row(AllMenu)

    info = gen_homework_info()[0][callback.data]
    await callback.message.edit_text(f"[{info[0]}]"
                                     f"({info[1]})",
                                     reply_markup=kb)


# @dp.callback_query_handlers(lambda x: x.data in gen_homework_info()[1], state=(FSMClient.video, None))
async def cb_homework_module2(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=3)
    kb.add(*gen_homework_button(callback.data))
    kb.row(AllMenu)

    info = gen_homework_info()[1][callback.data]
    await callback.message.edit_text(f"[{info[0]}]"
                                     f"({info[1]})",
                                     reply_markup=kb)


# @dp.callback_query_handlers(lambda x: x.data in gen_homework_info()[2], state=(FSMClient.video, None))
async def cb_homework_module3(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=3)
    kb.add(*gen_homework_button(callback.data))
    kb.row(AllMenu)

    info = gen_homework_info()[2][callback.data]
    await callback.message.edit_text(f"[{info[0]}]"
                                     f"({info[1]})",
                                     reply_markup=kb)


# @dp.callback_query_handlers(lambda x: x.data in gen_homework_info()[3], state=(FSMClient.homework, None))
async def cb_homework_module4(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=3)
    kb.add(*gen_homework_button(callback.data))
    kb.row(AllMenu)

    info = gen_homework_info()[3][callback.data]
    await callback.message.edit_text(f"[{info[0]}]"
                                     f"({info[1]})",
                                     reply_markup=kb)


def register_handlers_video(dp: Dispatcher):
    dp.register_callback_query_handler(cb_homework_module1, lambda x: x.data in gen_homework_info()[0],
                                       state=(FSMClient.homework, None))

    dp.register_callback_query_handler(cb_homework_module2, lambda x: x.data in gen_homework_info()[1],
                                       state=(FSMClient.homework, None))

    dp.register_callback_query_handler(cb_homework_module3, lambda x: x.data in gen_homework_info()[2],
                                       state=(FSMClient.homework, None))

    dp.register_callback_query_handler(cb_homework_module4, lambda x: x.data in gen_homework_info()[3],
                                       state=(FSMClient.homework, None))
