#
# Skeleton file for the Python "Hello World" exercise.
#
import time


def hello(name=''):
    return f"Hello, {name}!" if name else "Hello, World!"


def main():
    name = ''
    print hello(name)

main()
