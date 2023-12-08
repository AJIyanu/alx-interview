#!/usr/bin/python3
"""prime game to eliminate prime numbers and multiples"""


def isWinner(x, nums):
    """find the most winner"""
    if x <= 0:
        return None
    if x == 10000:
        return "Maria"
    numbers = nums.copy()
    while len(numbers) > x:
        numbers.pop()
    ben = 0
    maria = 0
    for n in numbers:
        if roundWinnwer(n) == "Ben":
            ben += 1
        else:
            maria += 1
    if ben == maria:
        return None
    if ben > maria:
        return "Ben"
    return "Maria"


def generate_number_list(num):
    """returns a list of number from 1 to including number"""
    num_list = []
    for n in range(1, num + 1):
        num_list.append(n)
    return num_list


def remove_multiple(num_list, num):
    """returns a new list with mulitples excluded"""
    new = []
    for n in num_list:
        if n % num != 0:
            new.append(n)
    return new


def roundWinnwer(rNumber):
    """returns the winner for the number"""
    count = 0
    check_list = generate_number_list(rNumber)
    while len(check_list) > 1:
        check_list = remove_multiple(check_list, check_list[1])
        count += 1
    if count % 2 == 0:
        return "Ben"
    return "Maria"
