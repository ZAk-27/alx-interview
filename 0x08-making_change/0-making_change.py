#!/usr/bin/python3
"""test module.
"""


def makeChange(coins, total):
    """Determining the fewest number of coins needed to meet a given amount total when given a pile of coins of different values.
    """
    if total <= 0:
        return 0
    rembrs = total
    coins_cmpt = 0
    coin_tot = 0
    sorted_coins = sorted(coins, reverse=True)
    n = len(coins)
    while rembrs > 0:
        if coin_tot >= n:
            return -1
        if rembrs - sorted_coins[coin_tot] >= 0:
            rembrs -= sorted_coins[coin_tot]
            coins_cmpt += 1
        else:
            coin_tot += 1
    return coins_count
