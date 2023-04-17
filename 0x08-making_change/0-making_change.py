#!/usr/bin/python3
"""
Find the lowest combinations of number of coin
"""


def makeChange(coins, total: int) -> int:
    """returns the lowest number of combination of coin"""
    if total <= 0:
        return 0
    count: int=0
    coins = sorted(coins, reverse=True)
    for coin in coins:
        check = int(total / coin)
        if check != 0:
            count += check
        total = total % coin
    return count if total == 0 else -1
