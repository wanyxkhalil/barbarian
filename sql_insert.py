#!/usr/bin/env python3

from _sql import insert_content

sql = 'insert into %s (%s) values (%s)'


def handle_fields(arr):
    return ['#{%s}' % x for x in arr]


if __name__ == '__main__':
    print(insert_content(sql, handle_fields))

