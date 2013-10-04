__author__ = 'shekhargulati'

import math

def sum_of_squares_of_n_natural_numbers(n):
    sum = 0;
    for i in range(1,n+1):
        sum += i*i
    return sum

def square_of_sum_of_n_natural_numbers(n):
    sum = 0
    for i in range(1,n+1):
        sum +=i
    return math.pow(sum,2)

if __name__ == "__main__":
    diff = square_of_sum_of_n_natural_numbers(100) - sum_of_squares_of_n_natural_numbers(100)
    print(diff)