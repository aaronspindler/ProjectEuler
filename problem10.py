import helpers


def summation_of_primes(limit):
    sum = 0
    primes = helpers.primes(limit)
    for prime in primes:
        sum += prime
    return sum

print(summation_of_primes(2000000))