from enum import Enum


RU_EN = {
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


class Layouts(Enum):
    RU = "RU"
    EN = "EN"


def convert(wrong_str: str, to_layout: Layouts):
    result_string = ""
    match to_layout:
        case Layouts.RU:
            result_string = __convert_string(wrong_str, RU_EN, True)
        case Layouts.EN:
            result_string = __convert_string(wrong_str, RU_EN, False)

    return result_string


def __convert_string(wrong_str: str, layout: dict[str, str], values_main: bool = True) -> str:
    default = layout
    reverted = revert_dict(layout)
    temp = ""
    for i in range(len(wrong_str)):
        if values_main:
            temp += (wrong_str[i] if not default.keys().__contains__(wrong_str[i]) else default.get(wrong_str[i])) if wrong_str[i].islower() else (wrong_str[i] if not default.keys().__contains__(wrong_str[i].lower()) else default.get(wrong_str[i].lower())).upper()
        else:
            temp += (wrong_str[i] if not reverted.keys().__contains__(wrong_str[i]) else reverted.get(wrong_str[i])) if wrong_str[i].islower() else (wrong_str[i] if not reverted.keys().__contains__(wrong_str[i].lower()) else reverted.get(wrong_str[i].lower())).upper()

    return temp


def revert_dict(_dict: dict[str, str]) -> dict[str, str]:
    reverted = {}

    for k, v in _dict.items():
        reverted[v] = k

    return reverted