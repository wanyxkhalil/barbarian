#!/usr/bin/env python3

from _sys import read


def underline_to_camel(underline_format):
    """
        下划线命名格式转驼峰命名格式
    """
    if not isinstance(underline_format, str):
        return None

    arr = underline_format.split('_')
    rest = [x.capitalize() for x in arr[1:]]

    return arr[0] + ''.join(rest)


if __name__ == '__main__':
    s = read('Please input string')
    print(underline_to_camel(s))
