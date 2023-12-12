from aiogram import types

Video = types.InlineKeyboardButton('Видео Уроки📼', callback_data='Video')
HomeWork = types.InlineKeyboardButton('Разбор Домашек🏠', callback_data='HomeWork')
Project = types.InlineKeyboardButton('Проекты🧠', callback_data='Project')
Book = types.InlineKeyboardButton('Текстовые материалы📚', callback_data='Book')
Learn = types.InlineKeyboardButton('Дополнительная практика🫡', callback_data='Learn')

Module1 = types.InlineKeyboardButton('Module1🤨', callback_data='Module1')
Module2 = types.InlineKeyboardButton('Module2🫠 ', callback_data='Module2')
Module3 = types.InlineKeyboardButton('Module3🤯', callback_data='Module3')
Module4 = types.InlineKeyboardButton('Module4🫣', callback_data='Module4')

AllMenu = types.InlineKeyboardButton('Вернуться в меню🔙', callback_data='Menu')

def gen_learn_button(callback: types.CallbackQuery) -> [list]:
    """
    :param callback: Выбранная категория
    :return: Список кнопок
    """

    kb = []
    kb_info = {
        'Level 1': 'Learn', 'Level 2': 'lvl2', 'Level 3': 'lvl3',
        'OOP': 'lvl5', 'LeetCode': 'lvl6', 'Codewars': 'lvl7',
        'Bioinformatics Institute': 'lvl4'
    }

    for name, call in kb_info.items():
        if call == callback:
            kb.append(types.InlineKeyboardButton(f"{name}🔷", callback_data=f"{call}"))
        else:
            kb.append(types.InlineKeyboardButton(f"{name}🔶", callback_data=f"{call}"))
    return kb
def gen_learn_info() -> [dict]:
    """
    :param callback: Ключ к словарю
    :return: Список с информацией
    """
    info = {
        'Learn': ['Для начинающих', 'https://telegra.ph/Codewars-03-17'],
        'lvl2': ['Для продвинутых', 'https://telegra.ph/Dlya-prodvinutyh-03-17'],
        'lvl3': ['Инди-курс', 'https://telegra.ph/Indi-kurs-03-17-2'],
        'lvl4': ['Bioinformatics Institute', 'https://telegra.ph/Bioinformatics-Institute-03-17'],
        'lvl5': ['Всё про ООП', 'https://telegra.ph/OOP-03-17'],
        'lvl6': ['LeetCode', 'https://telegra.ph/LeetCode-03-17'],
        'lvl7': ['Codewars', 'https://telegra.ph/Codewars-03-17-2']
    }
    return info


def gen_book_button(callback: types.CallbackQuery) -> [list]:
    """
    :param callback: Выбранная категория
    :return: Список кнопок
    """

    kb = []
    kb_info = {
        'Числа': 'Book', 'Строки': 'str', 'Списки': 'list',
        'Словари': 'dict', 'Turtle': 'turtle',
        'ООП': 'OOP', 'Чтение файлов': 'open'
    }

    for name, call in kb_info.items():
        if call == callback:
            kb.append(types.InlineKeyboardButton(f"{name}🔷", callback_data=f"{call}"))
        else:
            kb.append(types.InlineKeyboardButton(f"{name}🔶", callback_data=f"{call}"))
    return kb
def gen_book_info() -> [dict]:
    """
    :param callback: Ключ к словарю
    :return: Список с информацией
    """
    info = {
        'Book': ['Числа', 'https://telegra.ph/CHislovye-metodyfunkciioperacii-02-05'],
        'str': ['Строки', 'https://telegra.ph/Strokovye-metodyfunkciiprimery-02-05'],
        'list': ['Списки', 'https://telegra.ph/Metodyfunkciiprimery-spiskov-02-05'],
        'dict': ['Словари', 'https://telegra.ph/Primery-i-metody-slovarej-02-05'],
        'open': ['Чтение файлов', 'https://telegra.ph/CHtenie-fajlov-02-05'],
        'turtle': ['Turtle', 'https://telegra.ph/Modul-Turtle-02-05'],
        'OOP': ['ООП', 'https://telegra.ph/OOP-02-05'],
    }
    return info



