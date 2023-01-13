#!/usr/bin/python3
"""
This module does this
In a text file, there is a single character H.
Your text editor can execute only two operations
in this file: Copy All and Paste. Given a number
n, write a method that calculates the fewes
number of operations needed to result in exactly
n H characters in the file.
"""


def minOperations(n):
    """find minimum operation"""
    from math import sqrt
    def is_prime(number):
        """checks for prime"""
        if number == 2:
            return True
        sq_num = int(sqrt(number)) + 1
        if number % 2 == 0 or number % sq_num == 0:
            return False
        for i in range(2, sq_num):
            if number % i == 0:
                return False
        return True
    if is_prime(n):
        return n
    min_op = []
    div = 2
    while n > 1:
        if is_prime(div):
            if n % div == 0:
                min_op.append(div)
                n = n / div
            else:
                div = div + 1
        else:
            div = div + 1
    return sum(min_op)
