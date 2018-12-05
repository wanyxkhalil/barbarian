#!/usr/bin/env python3

from _sql import *
from str_camel_2_snake import camel_to_underline

sql = 'select %s from %s'


def handle_fields(arr):
    fields1 = [camel_to_underline(x) for x in arr]
    fields2 = ['#{%s}' % x for x in arr]

    return fields1, fields2


if __name__ == '__main__':
    s = read('Please paste class')
    table = parse_table(s)
    fields = parse_under_fields(s)

    print(sql % (','.join(fields), table))
