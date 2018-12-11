import sys


def read(s="Please input something"):
    print(s, "->")
    arr = [line for line in sys.stdin]
    return ''.join(arr)


def read_1_line(s="Please input something"):
    print(s, "->")
    return sys.stdin.readline()
