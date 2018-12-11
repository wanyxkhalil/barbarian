#!/usr/bin/env python3

import random
import string
from _sys import read_1_line


def random_word(n=40):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))


if __name__ == '__main__':
    line = read_1_line("Please input a number")
    print(random_word(int(line)))
