from _sys import read
import re
from str_camel_2_snake import camel_to_underline


def parse_table(s):
    return camel_to_underline(next(re.finditer(r' class (\w+) {', s)).groups()[0])


def parse_fields(s):
    body = next(re.finditer(r'{([\S\s]*)\}', s)).group()
    return re.findall(r'.* (\w+);', body)


def convert_fields_2_under(fields):
    return [camel_to_underline(x) for x in fields]


def parse_under_fields(s):
    fields = parse_fields(s)
    return convert_fields_2_under(fields)


def insert_out(sql, table, under_fields, class_fields):
    return sql % (table, ','.join(under_fields), ','.join(class_fields))


def insert_content(sql, fields_func):
    s = read('Please paste class')
    table = parse_table(s)
    fields = parse_fields(s)

    under_fields = convert_fields_2_under(fields)
    class_fields = fields_func(fields)

    return insert_out(sql, table, under_fields, class_fields)
