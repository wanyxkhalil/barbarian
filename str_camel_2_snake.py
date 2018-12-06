#!/usr/bin/env python3

from _sys import read


def camel_to_underline(camel_format):
    """
        驼峰命名格式转下划线命名格式
    """
    if not isinstance(camel_format, str):
        return None

    camel_format = camel_format.strip()
    rest = [x if x.islower() else '_' + x.lower() for x in camel_format[1:]]
    return camel_format[0].lower() + ''.join(rest)


if __name__ == '__main__':
    s = read('Please input string')
    print(camel_to_underline(s))
