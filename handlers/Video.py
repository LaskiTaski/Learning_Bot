from aiogram import Dispatcher
from keyboards.kb_Video import *
from handlers.FSM import FSMClient
from keyboards.kb_FSM import AllMenu


# @dp.callback_query_handlers(lambda x: x.data in gen_video_info()[0], state=(FSMClient.video, None))
async def cb_video_module1(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=3)
    kb.add(*gen_video_button(callback.data))
    kb.row(AllMenu)

    info = gen_video_info()[0][callback.data]
    await callback.message.edit_text(f"[{info[0]}]"
                                     f"({info[1]})",
                                     reply_markup=kb)


# @dp.callback_query_handlers(lambda x: x.data in gen_video_info()[1], state=(FSMClient.video, None))
async def cb_video_module2(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=3)
    kb.add(*gen_video_button(callback.data))
    kb.row(AllMenu)

    info = gen_video_info()[1][callback.data]
    await callback.message.edit_text(f"[{info[0]}]"
                                     f"({info[1]})",
                                     reply_markup=kb)


# @dp.callback_query_handlers(lambda x: x.data in gen_video_info()[2], state=(FSMClient.video, None))
async def cb_video_module3(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=3)
    kb.add(*gen_video_button(callback.data))
    kb.row(AllMenu)

    info = gen_video_info()[2][callback.data]
    await callback.message.edit_text(f"[{info[0]}]"
                                     f"({info[1]})",
                                     reply_markup=kb)


# @dp.callback_query_handlers(lambda x: x.data in gen_video_info()[3], state=(FSMClient.video, None))
async def cb_video_module4(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=3)
    kb.add(*gen_video_button(callback.data))
    kb.row(AllMenu)

    info = gen_video_info()[3][callback.data]
    await callback.message.edit_text(f"[{info[0]}]"
                                     f"({info[1]})",
                                     reply_markup=kb)


def register_handlers_video(dp: Dispatcher):
    dp.register_callback_query_handler(cb_video_module1, lambda x: x.data in gen_video_info()[0],
                                       state=(FSMClient.video, None))

    dp.register_callback_query_handler(cb_video_module2, lambda x: x.data in gen_video_info()[1],
                                       state=(FSMClient.video, None))

    dp.register_callback_query_handler(cb_video_module3, lambda x: x.data in gen_video_info()[2],
                                       state=(FSMClient.video, None))

    dp.register_callback_query_handler(cb_video_module4, lambda x: x.data in gen_video_info()[3],
                                       state=(FSMClient.video, None))
