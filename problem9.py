__author__ = 'shekhargulati'

import math
import sys
def is_pythagorean_triplet(a , b , c):
    return math.pow(c, 2) == math.pow(a , 2) + math.pow(b , 2)


if __name__ == "__main__":
    for m in range(2 , 1000):
        for n in range(1 , m-1):
            a = math.pow(m ,2) - math.pow(n,2)
            b = 2*m*n
            c = math.pow(m,2) + math.pow(n,2)
            if is_pythagorean_triplet(a , b, c) and (a +  b + c == 1000):
                print("a = %s , b = %s , c = %s" % (a , b , c))
                answer = a * b * c
                print(answer)
                sys.exit("Program finished")

