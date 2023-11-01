#!/usr/bin/python3
"""
The N queens puzzle is the challenge of placing N
non-attacking queens on an NxN chessboard.
Write a program that solves the N queens problem.

Usage: nqueens N
If the user called the program with the wrong number of arguments,
print Usage: nqueens N, followed by a new line,
and exit with the status 1
where N must be an integer greater or equal to 4
If N is not an integer, print N must be a number,
followed by a new line, and exit with the status 1
If N is smaller than 4, print N must be at least 4,
followed by a new line, and exit with the status 1
The program should print every possible solution to the problem
One solution per line
Format: see example
You don't have to print the solutions in a specific order
You are only allowed to import the sys module
"""

import sys


def create_positions(n: int) -> list:
    """returns a list of possible positions"""
    posible = []
    for i in range(n):
        for j in range(n):
            posible.append([i, j])
    return posible

def cancel_VH(full_list: list, post: list):
    """
    returns a new list with vertical and diagonal
    position canceled out
    """
    new_list = []
    for each in full_list:
        if each[0] != post[0] and each[1] != post[1]:
            new_list.append(each)
    return new_list

def visual(positions, num):
    """prints postion in a visible manner"""
    count = 0
    for each in positions:
        if count == num - 1:
            if each[1] != num:
                print("[x, x]")
            print(each)
            count = 0
        else:
            if each[1] != num:
                print(f"[x, x] ", end="")
            print(f"{each} ", end="")
            count += 1


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: nqueens N")
        exit(1)
    try:
        num = int(sys.argv[1])
        if num < 4:
            print("N must be at least 4")
            exit(1)
    except ValueError:
        print("N must be a number")
        exit(1)
    check = cancel_VH(create_positions(num), [0, 0])
    print(check)
    visual(check, num)
