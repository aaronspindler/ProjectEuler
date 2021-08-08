def largest_prime_factor(input):
    factors = []
    divisor = 2
    while input > 1:
        while input % divisor == 0:
            factors.append(divisor)
            input /= divisor
        divisor += 1

        if divisor*divisor > input:
            if input > 1:
                factors.append(input)
            break

    return max(factors)

print(largest_prime_factor(600851475143))