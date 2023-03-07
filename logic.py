from enum import Enum

__RU_EN = {
    "q": "й",
    "w": "ц",
    "e": "у",
    "r": "к",
    "t": "е",
    "y": "н",
    "u": "г",
    "i": "ш",
    "o": "щ",
    "p": "з",
    "[": "х",
    "]": "ъ",
    "a": "ф",
    "s": "ы",
    "d": "в",
    "f": "а",
    "g": "п",
    "h": "р",
    "j": "о",
    "k": "л",
    "l": "д",
    ";": "ж",
    "'": "э",
    "z": "я",
    "x": "ч",
    "c": "с",
    "v": "м",
    "b": "и",
    "n": "т",
    "m": "ь",
    ",": "б",
    ".": "ю",
    "/": ".",
    "?": ",",
    "Q": "Й",
    "W": "Ц",
    "E": "У",
    "R": "К",
    "T": "Е",
    "Y": "Н",
    "U": "Г",
    "I": "Ш",
    "O": "Щ",
    "P": "З",
    "{": "Х",
    "}": "Ъ",
    "A": "Ф",
    "S": "Ы",
    "D": "В",
    "F": "А",
    "G": "П",
    "H": "Р",
    "J": "О",
    "K": "Л",
    "L": "Д",
    ":": "Ж",
    '"': "Э",
    "Z": "Я",
    "X": "Ч",
    "C": "С",
    "V": "М",
    "B": "И",
    "N": "Т",
    "M": "Ь",
    "<": "Б",
    ">": "Ю"
}
"""Словарь, содержащий в качестве пар ключ-значение пары символов (RU, EN), которые присутствуют в qwerty раскладке на клавиатуре."""


class Languages(Enum):
    """Класс-енам, содержащий в себе доступные в приложении языки для перевода."""

    RU = "russian"
    EN = "english"


def convert(wrong_str: str, current_language: Languages) -> str:
    """Конвертация раскладки строки. Является оберткой.

    Args:
        wrong_str (str): Строка в неправильной раскладке
        current_language (Languages): Язык, в который мы хотим переконвертировать строку.

    Returns:
        str: Строка на заданном языке.
    """
    result_string = ""
    match current_language:
        case Languages.EN:
            result_string = __convert_string(wrong_str, __RU_EN, True)
        case Languages.RU:
            result_string = __convert_string(wrong_str, __RU_EN, False)

    return result_string


def __convert_string(wrong_str: str, layout: dict[str, str], values_main: bool = True) -> str:
    """Конвертация раскладки строки. Содержит логику.

    Args:
        wrong_str (str): Строка в неправильной раскладке.
        layout (dict[str, str]): Словарь, содержащий пары символов необходимых раскладок.
        values_main (bool, optional): Флаг, указывающий на то, необходимо ли инвертировать словарь (Инвертирование словаря происходит, когда символы языка, в который мы хотим перевести строку, являются ключами словаря.). Для инвертирования необходимо передать False. Defaults to True.

    Returns:
        str: Строка в правильной раскладке.
    """

    needed_layout = None
    if values_main:
        needed_layout = layout
    else:
        needed_layout = __revert_dict(layout)
    temp = ""
    for i in range(len(wrong_str)):
        temp += (wrong_str[i] if not needed_layout.keys().__contains__(wrong_str[i]) else needed_layout.get(wrong_str[i]))

    return temp


def __revert_dict(_dict: dict[str, str]) -> dict[str, str]:
    """Получения инвертированного словаря.

    Args:
        _dict (dict[str, str]): Исходный словарь.

    Returns:
        dict[str, str]: Инвертированный словарь.
    """

    reverted = {}

    for k, v in _dict.items():
        reverted[v] = k

    return reverted


def detect_language(source_str: str) -> Languages:
    """Определение языка строки.

    Args:
        source_str (str): Исходная строка.

    Returns:
        Languages: Язык строки.
    """

    pass