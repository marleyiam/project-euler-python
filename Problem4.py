__author__ = 'shekhargulati'

import  math

def find_largest_six_digit_palindrome():
    for i in range(999999, 100000 ,-1):
        if is_palindrome(i):
            print("Palindrome number %s " % i)
            all_factors = factors(i)
            three_digit_factors = []
            for factor in all_factors:
                if factor >= 100 and factor <=999:
                    three_digit_factors.append(factor)
            reverse_three_digit_factors = sorted(three_digit_factors)[::-1]

            print(reverse_three_digit_factors)
            for x in reverse_three_digit_factors:
                for y in reverse_three_digit_factors:
                    if x *y == i:
                        print("Largest Palindrome %s" % i)
                        return i;



def is_palindrome(number):
    return str(number) == str(number)[::-1]

def factors(number):
	factors = {1}
	for i in range(2 , int(math.sqrt(number))+1):
		if number % i == 0:
			factors.add(i)
			factors.add(number/i)
	return factors
