#!/usr/bin/python3
"""
Defines the makeChange function
"""

def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
        coins (list): The denominations of the coins available.
        total (int): The target amount.

    Returns:
        int: Fewest number of coins needed, or -1 if the total cannot be met.
    """
    if total <= 0:
        return 0
    
    # Sort the coins in descending order
    coins.sort(reverse=True)
    count = 0

    for coin in coins:
        if total == 0:
            break
        if coin <= total:
            count += total // coin
            total %= coin

    return count if total == 0 else -1
