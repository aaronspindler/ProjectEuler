from math import ceil, log


def upper_bound(n):
    if n < 6:
        return 100
    return ceil(n * (log(n) + log(log(n))))


def find_primes(max):
    max = max+1
    primes = [2]
    not_primes = set()

    for i in range(3, max+1, 2):
        if i in not_primes:
            continue

        for j in range(i*3, max+1, i*2):
            not_primes.add(j)

        primes.append(i)
    return primes


def n_prime(n):
    return find_primes(upper_bound(n))[n-1]
