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
    "?": ","
}


class Languages(Enum):
    RU = "russian"
    EN = "english"


def convert(wrong_str: str, current_language: Languages):
    result_string = ""
    match current_language:
        case Languages.EN:
            result_string = __convert_string(wrong_str, __RU_EN, True)
        case Languages.RU:
            result_string = __convert_string(wrong_str, __RU_EN, False)

    return result_string


def __convert_string(wrong_str: str, layout: dict[str, str], values_main: bool = True) -> str:
    needed_layout = None
    if values_main:
        needed_layout = layout
    else:
        needed_layout = __revert_dict(layout)
    temp = ""
    for i in range(len(wrong_str)):
        temp += (wrong_str[i] if not needed_layout.keys().__contains__(wrong_str[i]) else needed_layout.get(wrong_str[i])) if wrong_str[i].islower() else (wrong_str[i] if not needed_layout.keys().__contains__(wrong_str[i].lower()) else needed_layout.get(wrong_str[i].lower())).upper()

    return temp


def __revert_dict(_dict: dict[str, str]) -> dict[str, str]:
    reverted = {}

    for k, v in _dict.items():
        reverted[v] = k

    return reverted


def detect_language(source_str: str) -> Languages:
    pass