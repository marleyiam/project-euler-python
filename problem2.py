def sumOfEvenFibonacciTerms(max):
    first = 1
    second = 1
    sum = 0
    while(second < max):
        if second %2 == 0:
            sum += second
        next_number = first + second
        first = second
        second = next_number
        
    return sum
