__author__ = 'shekhargulati'

import math


def find_nth_prime_no(n):
    prime_count = 2
    prime_number = 3
    answer = prime_number
    while prime_count < n:
        answer += 2
        if is_prime(answer):
            prime_count += 1
    return answer


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
    print(find_nth_prime_no(10001))
