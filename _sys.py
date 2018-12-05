import sys


def read(s):
    print(s, ":\n")
    arr = [line for line in sys.stdin]
    return ''.join(arr)

