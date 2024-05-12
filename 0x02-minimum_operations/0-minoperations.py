#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """Function to find the minimum number of operations needed."""
    min_operations = 0
    divisor = 2
    while isinstance(n, int) and n > 1:
        while n % divisor:
            divisor += 1
        min_operations += divisor
        n = int(n / divisor)
    return min_operations
