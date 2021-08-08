def div_checker(num, max):
    for divisor in range(1, max+1):
        if num % divisor == 0:
            continue
        else:
            return False
    return True


def smallest_divisable_by_range(max):
    num = 2
    while not div_checker(num, max):
        num += 1
    return num
