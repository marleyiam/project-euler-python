__author__ = 'shekhargulati'


def chain(number):
    elements = []
    while number > 1:
        if isEven(number):
            number = number / 2
            elements.append(number)
        elif isOdd(number):
            number = 3 * number + 1
            elements.append(number)
    return elements


def isEven(number):
    return number % 2 == 0


def isOdd(number):
    return number % 2 != 0


if __name__ == "__main__":
    start_number = 0
    number_of_elements = 0
    result = 0
    while start_number < 1000000:
        chain_elements = chain(start_number)
        #print(chain_elements)
        chain_length = len(chain_elements)
        if number_of_elements < len(chain_elements):
            number_of_elements = chain_length
            result = start_number
        start_number += 1
    print(result)



