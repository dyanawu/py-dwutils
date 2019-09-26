#!/usr/bin/python3

from math import sqrt, ceil

number = int(input())

def is_prime(x):
    if x >= 2:
        for y in range(2, x):
            if x % y == 0:
                return False
    return True

def smol_prime(n):
    limit = ceil(sqrt(n)) + 1
    return [x for x in range (2, n) if is_prime(x)]

def sieve(number):
    sieve = smol_prime(number)
    if number in sieve:
        return True
    is_prime = [number % x for x in sieve]
    return all(is_prime)

print(sieve(number))
