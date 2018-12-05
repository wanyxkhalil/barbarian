#!/usr/bin/env python3

from _sql import insert_content

sql = '<script>insert into %s (%s) values <foreach collection=\"list\" item=\"a\" index= \"index\" separator =\",' \
       '\">(%s)</foreach></script>'


def handle_fields(arr):
    return ['#{a.%s}' % x for x in arr]


if __name__ == '__main__':
    print(insert_content(sql, handle_fields))
