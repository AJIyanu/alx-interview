#!/usr/bin/python3
"""
Find the lowest combinations of number of coin
"""


def makeChange(coins, total: int) -> int:
    """
    Returns the minimum number of coins needed to make up the total amount.

    Args:
        coins (list[int]): List of integers representing the denominations of
        available coins.
        total (int): The total amount of money for which the minimum number
        of coins needs to be calculated.

    Returns:
        int: The minimum number of coins needed to make up the total amount,
        or -1 if it is not possible.
    """
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
