#!/usr/bin/python3
""" Module for solving prime game question """

def calculate_grundy(n):
    """ Module for solving prime game question """
    grundy = [0] * (n + 1)
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    
    for p in range(2, n + 1):
        if is_prime[p]:
            for multiple in range(p * p, n + 1, p):
                is_prime[multiple] = False
                grundy[multiple] = grundy[multiple // p] + 1
    
    for i in range(2, n + 1):
        if is_prime[i]:
            grundy[i] = 1
    
    return grundy

def isWinner(x, nums):
    """ Module for solving prime game question """
    wins_maria = 0
    wins_ben = 0
    
    for n in nums:
        grundy = calculate_grundy(n)
        xor_sum = 0
        for i in range(1, n + 1):
            xor_sum ^= grundy[i]
        
        if xor_sum == 0:
            wins_ben += 1
        else:
            wins_maria += 1
    
    if wins_maria > wins_ben:
        return "Maria"
    elif wins_ben > wins_maria:
        return "Ben"
    else:
        return None
