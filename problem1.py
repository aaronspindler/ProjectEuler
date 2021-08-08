def sum_multi_3_and_5(input):
    sum = 0
    for num in range(input):
        if not num % 3 == 0 and not num % 5 == 0:
            continue
        sum += num
    return sum
