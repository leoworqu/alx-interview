#!/usr/bin/python3
"""determines the fewest number of coins needed to meet a given amount total.
"""


def makeChange(coins, total):
    """function
    """
    if total < 0:
        return -1
    if total == 0:
        return 0
    
    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    
    for coin in coins:
        for j in range(coin, total + 1):
            if dp[j - coin] != float('inf'):
                dp[j] = min(dp[j], dp[j - coin] + 1)
    
    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
