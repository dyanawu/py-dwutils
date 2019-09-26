#!/usr/bin/python3

def is_prime(x):
    if x >= 2:
        for y in range(2, x):
            if x % y == 0:
                return False
    return True

def smol_prime(n):
    from math import sqrt, ceil
    limit = ceil(sqrt(n)) + 2
    return [x for x in range (2, limit) if is_prime(x)]

def greek_sift(number):
    bucket = list(range(1, number +1))
    print(f"Range to test:", bucket)
    sieve = smol_prime(number)
    print("Sieve: ", sieve)
    for prime in sieve:
        bucket = list(x if (x % prime or x == prime) and x > 1 else 0 for x in bucket)
        print(f"Multis of {prime}:", bucket)
    return None
    
if __name__ == "__main__":
    number = int(input())
    greek_sift(number)
