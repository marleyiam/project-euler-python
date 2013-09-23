#Project Euler Problem 3#
"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

import math
import time

def find_largest_prime_factor(number):
	start_time = time.time()
	prime_factors = [factor for factor in factors(number) if isPrime(factor)]
	result = sorted(prime_factors)[-1]
	print time.time() - start_time, "seconds"
	return result

def factors(number):
	factors = {1}
	for i in range(2 , int(math.sqrt(number))+1):
		if number % i == 0:
			factors.add(i)
			factors.add(number/i)
	return factors

def isPrime(number):
	if number <=1:
		return False
	if number == 2:
		return True
	if number % 2 == 0:
		return False
	for i in range(3, int(math.sqrt(number))+1, 2):
		if number % i == 0:
			return False
	return True