__author__ = 'shekhargulati'

def is_palindrome(number):
    return str(number) == str(number)[::-1]

def find_palindrome():
    palindrome = 0
    for i in range(1000 ,100 ,-1):
        for j in range(1000 , 100 ,-1):
            if is_palindrome(i*j):
                if i*j > palindrome:
                    palindrome = i*j
    return palindrome


if __name__ == "__main__":
    print(find_palindrome())