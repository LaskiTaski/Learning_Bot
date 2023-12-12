from aiogram import Dispatcher
from keyboards.kb_Project import *
from handlers.FSM import FSMClient
from keyboards.kb_FSM import AllMenu


# @dp.callback_query_handlers(lambda x: x.data in gen_project_info()[0], state=(FSMClient.project, None))
async def cb_project_module1(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=3)
    kb.add(*gen_project_button(callback.data))
    kb.row(AllMenu)

    info = gen_project_info()[0][callback.data]
    await callback.message.edit_text(f"[{info[0]}]"
                                     f"({info[1]})",
                                     reply_markup=kb)


# @dp.callback_query_handlers(lambda x: x.data in gen_project_info()[1], state=(FSMClient.project, None))
async def cb_project_module2(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=3)
    kb.add(*gen_project_button(callback.data))
    kb.row(AllMenu)

    info = gen_project_info()[1][callback.data]
    await callback.message.edit_text(f"[{info[0]}]"
                                     f"({info[1]})",
                                     reply_markup=kb)


# @dp.callback_query_handlers(lambda x: x.data in gen_project_info()[2], state=(FSMClient.project, None))
async def cb_project_module3(callback: types.CallbackQuery):
    kb = types.InlineKeyboardMarkup(row_width=3)
    kb.add(*gen_project_button(callback.data))
    kb.row(AllMenu)

    info = gen_project_info()[2][callback.data]
    await callback.message.edit_text(f"[{info[0]}]"
                                     f"({info[1]})",
                                     reply_markup=kb)


def register_handlers_video(dp: Dispatcher):
    dp.register_callback_query_handler(cb_project_module1, lambda x: x.data in gen_project_info()[0],
                                       state=(FSMClient.project, None))

    dp.register_callback_query_handler(cb_project_module2, lambda x: x.data in gen_project_info()[1],
                                       state=(FSMClient.project, None))

    dp.register_callback_query_handler(cb_project_module3, lambda x: x.data in gen_project_info()[2],
                                       state=(FSMClient.project, None))