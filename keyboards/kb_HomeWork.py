from aiogram import types


def gen_homework_button(callback: types.CallbackQuery) -> [list]:
    """
    :param callback: Выбранная категория
    :return: Список кнопок
    """
    kb = []
    kb_info = {
        '1 Урок': f'Module{callback[-1]}', '2 Урок': f'lesson_2_{callback[-1]}',
        '3 Урок': f'lesson_3_{callback[-1]}', '4 Урок': f'lesson_4_{callback[-1]}',
        '5 Урок': f'lesson_5_{callback[-1]}', '6 Урок': f'lesson_6_{callback[-1]}',
        '7 Урок': f'lesson_7_{callback[-1]}', '8 Урок': f'lesson_8_{callback[-1]}',
        '9 Урок': f'lesson_9_{callback[-1]}', '10 Урок': f'lesson_10_{callback[-1]}',
        '11 Урок': f'lesson_11_{callback[-1]}', '12 Урок': f'lesson_12_{callback[-1]}',
    }
    for name, call in kb_info.items():
        if call == callback:
            kb.append(types.InlineKeyboardButton(f"{name}🔷", callback_data=f"{call}"))
        else:
            kb.append(types.InlineKeyboardButton(f"{name}🔶", callback_data=f"{call}"))
    return kb


def gen_homework_info() -> [dict]:
    """
    :param callback: Ключ к словарю
    :return: Список с информацией
    """
    info = [
        {
            'Module1': ['1 Урок', 'https://telegra.ph/Modul-1-Urok-1-10-15'],
            'lesson_2_1': ['2 Урок', 'https://telegra.ph/Modul-1-Urok-2-10-15'],
            'lesson_3_1': ['3 Урок', 'https://telegra.ph/Modul-1-Urok-3-10-15'],
            'lesson_4_1': ['4 Урок', 'https://telegra.ph/Modul-1-Urok-4-10-15'],
            'lesson_5_1': ['5 Урок', 'https://telegra.ph/Modul-1-Urok-5-10-15'],
            'lesson_6_1': ['6 Урок', 'https://telegra.ph/Modul-1-Urok-6-10-15'],
            # 'lesson_7_1': ['7 Урок', 'https://telegra.ph/Modul-1-Urok-7-02-03'],
            # 'lesson_8_1': ['8 Урок', 'https://telegra.ph/Modul-1-Urok-8-02-03'],
            # 'lesson_9_1': ['9 Урок', 'https://telegra.ph/Modul-1-Urok-9-02-03'],
            # 'lesson_10_1': ['10 Урок', 'https://telegra.ph/Modul-1-Urok-10-02-03'],
            # 'lesson_11_1': ['11 Урок', 'https://telegra.ph/Modul-1-Urok-11-02-03'],
            # 'lesson_12_1': ['12 Урок', 'https://telegra.ph/Modul-1-Urok-12-02-03'],
        },
        {
            # 'Module2': ['1 Урок', 'https://telegra.ph/Modul-2-Urok-1-02-03'],
            # 'lesson_2_2': ['2 Урок', 'https://telegra.ph/Modul-2-Urok-2-02-03'],
            # 'lesson_3_2': ['3 Урок', 'https://telegra.ph/Modul-2-Urok-3-02-03'],
            # 'lesson_4_2': ['4 Урок', 'https://telegra.ph/Modul-2-Urok-4-02-03'],
            # 'lesson_5_2': ['5 Урок', 'https://telegra.ph/Modul-2-Urok-5-02-03'],
            # 'lesson_6_2': ['6 Урок', 'https://telegra.ph/Modul-2-Urok-6-02-03'],
            # 'lesson_7_2': ['7 Урок', 'https://telegra.ph/Modul-2-Urok-7-02-03'],
            # 'lesson_8_2': ['8 Урок', 'https://telegra.ph/Modul-2-Urok-8-02-03'],
            # 'lesson_9_2': ['9 Урок', 'https://telegra.ph/Modul-2-Urok-9-02-03'],
            # 'lesson_10_2': ['10 Урок', 'https://telegra.ph/Modul-2-Urok-10-02-03'],
            # 'lesson_11_2': ['11 Урок', 'https://telegra.ph/Modul-2-Urok-11-02-03'],
            # 'lesson_12_2': ['12 Урок', 'https://telegra.ph/Modul-2-Urok-12-02-03']
        },
        {
            # 'Module3': ['1 Урок', 'https://telegra.ph/Modul-3-Urok-1-03-17'],
            # 'lesson_2_3': ['2 Урок', 'https://telegra.ph/Modul-3-Urok-2-03-17-2'],
            # 'lesson_3_3': ['3 Урок', 'https://telegra.ph/Modul-3-Urok-3-03-18'],
            # 'lesson_4_3': ['4 Урок', 'https://telegra.ph/Modul-3-Urok-4-03-18'],
            # 'lesson_5_3': ['5 Урок', 'https://telegra.ph/Modul-3-Urok-5-03-18-2'],
            # 'lesson_6_3': ['6 Урок', 'https://telegra.ph/Modul-3-Urok-6-03-18'],
            # 'lesson_7_3': ['7 Урок', 'https://telegra.ph/Modul-3-Urok-7-03-18'],
            # 'lesson_8_3': ['8 Урок', 'https://telegra.ph/Modul-3-Urok-8-03-18'],
            # 'lesson_9_3': ['9 Урок', 'https://telegra.ph/Modul-3-Urok-9-03-19'],
            # 'lesson_10_3': ['10 Урок', 'https://telegra.ph/Modul-3-Urok-10-03-19'],
            # 'lesson_11_3': ['11 Урок', 'https://telegra.ph/Modul-3-Urok-11-03-19'],
            # 'lesson_12_3': ['12 Урок', 'https://telegra.ph/Modul-3-Urok-12-03-19'],
        },
        {
            # 'Module4': ['1 Урок', ''],
            # 'lesson_2_4': ['2 Урок', ''],
            # 'lesson_3_4': ['3 Урок', ''],
            # 'lesson_4_4': ['4 Урок', ''],
            # 'lesson_5_4': ['5 Урок', ''],
            # 'lesson_6_4': ['6 Урок', ''],
            # 'lesson_7_4': ['7 Урок', ''],
            # 'lesson_8_4': ['8 Урок', ''],
            # 'lesson_9_4': ['9 Урок', ''],
            # 'lesson_10_4': ['10 Урок', ''],
            # 'lesson_11_4': ['11 Урок', ''],
            # 'lesson_12_4': ['12 Урок', '']
        }
    ]

    return info
