def is_prime(x):
    if x >= 2:
        for y in range(2, x):
            if x % y == 0:
                return False
    return True

def smol_prime(n):
    from math import sqrt, ceil
    limit = ceil(sqrt(n)) + 1
    return [x for x in range (2, limit) if is_prime(x)]

def sieve_one(number):
    sieve = smol_prime(number)
    if number in sieve:
        return True
    is_prime = [number % x for x in sieve]
    return all(is_prime)

def gen_primes(number):
    sieve = smol_prime(number)
    primes = []

    for x in range(2, number + 1):
        if x in sieve:
            primes.append(x)
        else:
            isprime = [x % y for y in sieve]
            if all(isprime):
                primes.append(x)

    return primes

if __name__ == "__main__":
    number = int(input())
    print(gen_primes(number))
