__author__ = 'shekhargulati'

import math


def factors(number):
    factors = {1}
    for i in range(2, int(math.sqrt(number)) + 1):
        if number % i == 0:
            factors.add(i)
            factors.add(number / i)
    return factors


if __name__ == "__main__":
    number_of_divisors = 0
    start_number = 1000
    triangular_number = 0
    while number_of_divisors < 501:
        triangular_number = sum(range(1, start_number))
        number_of_divisors = len(factors(triangular_number))
        start_number += 1
    print(triangular_number)





