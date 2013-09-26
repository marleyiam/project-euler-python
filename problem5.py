__author__ = 'shekhargulati'

import time

def problem5(number):

    for i in range(11 , 21):
        if number % i != 0:
            return False
    return True


if __name__ == "__main__":
    start_time = time.time();
    number = 2520
    while not problem5(number):
        number +=2520
    print(number)
    print('Program took {} {}'.format(time.time() - start_time , "sec(s)"))