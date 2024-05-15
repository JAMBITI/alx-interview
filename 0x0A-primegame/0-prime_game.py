#!/usr/bin/python3
"""module for functions"""

def sieve_of_eratosthenes(n):
    """Return a list of boolean values indicating primality."""
    if n < 2:
        return [False] * (n + 1)
    prime = [True] * (n + 1)
    prime[0] = prime[1] = False
    for p in range(2, int(n**0.5) + 1):
        if prime[p]:
            for i in range(p * p, n + 1, p):
                prime[i] = False
    return prime

def countPrime(n):
    """Count the number of prime numbers up to n."""
    prime = sieve_of_eratosthenes(n)
    return sum(prime)

def isWinner(x, nums):
    """Determine the winner based on prime number count."""
    if x <= 0 or not nums:
        return None

    ben, maria = 0, 0
    for i in range(x):
        if countPrime(nums[i]) % 2 == 0:
            ben += 1
        else:
            maria += 1

    if ben > maria:
        return "Ben"
    elif maria > ben:
        return "Maria"
    return None
