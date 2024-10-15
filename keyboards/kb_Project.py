from aiogram import types


def gen_project_button(callback: types.CallbackQuery) -> [list]:
    """
    :param callback: Выбранная категория
    :return: Список кнопок
    """
    kb = []
    kb_info = {
        '1 Проект': f'Module{callback[-1]}',
        '2 Проект': f'lesson_2_{callback[-1]}',
        '3 Проект': f'lesson_3_{callback[-1]}',
    }
    for name, call in kb_info.items():
        if call == callback:
            kb.append(types.InlineKeyboardButton(f"{name}🔷", callback_data=f"{call}"))
        else:
            kb.append(types.InlineKeyboardButton(f"{name}🔶", callback_data=f"{call}"))
    return kb


def gen_project_info() -> [dict]:
    """
    :param callback: Ключ к словарю
    :return: Список с информацией
    """
    info = [
        {
            'Module1': ['10 Урок', 'https://telegra.ph/Pervyj-proekt-1-modulya-02-03'],
            'lesson_2_1': ['11 Урок', 'https://telegra.ph/Vtoroj-proekt-1-modulya-02-03'],
            'lesson_3_1': ['3 Урок', 'https://telegra.ph/Tretij-proekt-1-modulya-02-03']
        },
        {
            'Module2': ['8 Урок', 'https://telegra.ph/Pervyj-proekt-2-modulya-02-03'],
            'lesson_2_2': ['11 Урок', 'https://telegra.ph/Vtoroj-proekt-2-modulya-02-03'],
            'lesson_3_2': ['12 Урок', 'https://telegra.ph/Tretij-proekt-2-modulya-02-03']
        },
        {
            'Module3': ['12 Урок', 'https://telegra.ph/Mini-bot-03-17'],
        },
    ]

    return info
