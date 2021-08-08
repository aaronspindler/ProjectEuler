import math


def sum_square_difference(max):
    sum_squares = 0
    sum = 0
    for x in range(max+1):
        sum_squares += math.pow(x, 2)
        sum += x

    square_of_the_sum = math.pow(sum, 2)

    return int(square_of_the_sum - sum_squares)
