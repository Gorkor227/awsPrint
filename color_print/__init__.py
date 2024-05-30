# !/usr/bin/env python
# -*- coding: utf-8 -*-
# ------------------------------
""""""
from .color_print import cp
from typing import Union
from typing_extensions import Self


class FontColor:
    black = '\x1b[30m'
    red = '\x1b[31m'
    green = '\x1b[32m'
    yellow = '\x1b[33m'
    blue = '\x1b[34m'
    magenta = '\x1b[35m'
    cyan = '\x1b[36m'
    white = '\x1b[37m'
    reset = '\x1b[39m'
    BLACK = '\x1b[90m'
    RED = '\x1b[91m'
    GREEN = '\x1b[92m'
    YELLOW = '\x1b[93m'
    BLUE = '\x1b[94m'
    MAGENTA = '\x1b[95m'
    CYAN = '\x1b[96m'
    WHITE = '\x1b[97m'


class PformatSettingsMeta(type):
    def __getitem__(cls, key):
        if hasattr(cls, key):
            return getattr(cls, key)
        else:
            raise KeyError(f"'{cls.__name__}' object has no attribute '{key}'")

    def __setitem__(cls, key, value):
        setattr(cls, key, value)


class PformatSettings(metaclass=PformatSettingsMeta):
    indent = 1
    width = 80
    depth = None
    compact = False
    sort_dicts = True
    underscore_numbers = False

    @classmethod
    def __class_getitem__(cls, item):
        return getattr(cls, item)

    def __setattr__(self, key, value):
        setattr(self.__class__, key, value)


class CPrint:
    def __init__(self):
        self.default_color = FontColor.YELLOW

    def set_default_color(self, color) -> None:
        self.default_color = color

    def __call__(self, *values: object, sep: Union[str, None] = ' ', end: Union[str, None] = '\n', file=None,
                 color=None, isFormat=False) -> Self:
        if len(values) > 0:
            if isFormat:
                from pprint import pformat
                values = (pformat(object=val, indent=PformatSettings.indent, width=PformatSettings.width,
                                  depth=PformatSettings.depth, compact=PformatSettings.compact,
                                  sort_dicts=PformatSettings.sort_dicts,
                                  underscore_numbers=PformatSettings.underscore_numbers) for val in values)

            cp(*values, sep=sep, end=end, file=file, color=color or self.default_color)
        else:
            print()

        return self


def print(*values: object, sep: Union[str, None] = ' ', end: Union[str, None] = '\n', file=None,
          color=None, isFormat: bool = False) -> CPrint:
    """
    todo Extended implementation of python’s built-in print function
    :param values: same as print()
    :param sep: same as print()
    :param end: same as print()
    :param file: same as print()
    :param color: Yellow  --> FontColor's attr
    :param isFormat: False   --> By pprint.pformat
    :return:
    """
    if not values:
        values = '',
    return CPrint()(*values, sep=sep, end=end, file=file, isFormat=isFormat, color=color or FontColor.YELLOW)
