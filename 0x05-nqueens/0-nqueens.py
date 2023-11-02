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

def cancel_diag(full_list: list, post: list) -> list:
    """
    returns a new list with diagonals
    removed left right up down
    """
    new_list = []
    list2 = []
    for each in full_list:
        diff = post[0] - each[0]
        if post[1] - diff != each[1]:
            new_list.append(each)
    for each in new_list:
        diff = post[0] - each[0]
        if post[1] + diff != each[1]:
            list2.append(each)
    return list2

def remove_invalid(lst: list, pos: list):
    """returns a new list valid for other queens to stand"""
    vhout = cancel_VH(lst, pos)
    diagout = cancel_diag(vhout, pos)
    return diagout

def visual(pos, num):
    """prints postion in a visible manner"""
    z = 0
    for x in range(num):
        for y in range(num):
            try:
                if x == pos[z][0] and y == pos[z][1]:
                    print(f"{pos[z]} ", end="")
                    z += 1
                else:
                    print("[X, X] ", end="")
            except IndexError:
                print("[X, X] ", end="")
        print()


def arrange_queens(possible: list, num: int):
    """returns all posible poitions of queens
       without taking each other out"""
    grand_list = []
    trash = possible.copy()
    for y in range(num):
        sub_list = []
        for x in range(num):
            print(f"chcking out {[x,y]} in {trash}")
            if [x, y] in trash:
                print(f"found {[x, y]}")
                sub_list.append([x, y])
                trash = remove_invalid(trash, [x, y])
                visual(trash, num)
        grand_list.append(sub_list)
    return grand_list


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
    check = arrange_queens(create_positions(num), num)
    for each in check:
        visual(each, num)
        print(len(each))
        print()
