__author__ = 'shekhargulati'

import math;


def is_prime(number):
    if number <= 1:
        return False
    if number == 2:
        return True
    if number % 2 == 0:
        return False
    for i in range(3, int(math.sqrt(number)) + 1, 2):
        if number % i == 0:
            return False
    return True


if __name__ == "__main__":
    sum = 2
    for i in range(3 , 2000000 , 2):
        if is_prime(i):
            sum += i
    print(sum)