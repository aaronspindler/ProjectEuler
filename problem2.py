def fib_sum_even(limit):
    sum = 2

    prev = 1
    current = 2

    while current < limit:
        temp = current
        current = temp + prev
        prev = temp
        if current % 2 == 0:
            sum += current

    return sum
