#!/usr/bin/env python3
fibonacci_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

def print_fibonacci(length):
    numbers = ([num for num in fibonacci_list[0:length]])
    print(numbers)