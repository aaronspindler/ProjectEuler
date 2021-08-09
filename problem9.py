import math


def pythagorean_triplet():
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = 1000 - a - b
            if math.pow(a, 2) + math.pow(b, 2) == math.pow(c, 2):
                return a*b*c

print(pythagorean_triplet())