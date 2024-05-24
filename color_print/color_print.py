from typing import Union

__default__ = '\x1b[93m'


def cp(*values: object, sep: Union[str, None] = ' ', end: Union[str, None] = '\n', file=None,
       color=__default__):
    args_0, *arg = values

    print(color + str(args_0), *arg, sep=sep, end=end, file=file)
