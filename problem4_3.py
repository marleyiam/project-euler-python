__author__ = 'shekhargulati'

def is_palindrome(number):
    return str(number) == str(number)[::-1]

def find_palindrome():
    palindrome = 0
    i = 1000
    while i >= 100:
        j = i
        while j >= 100:
            possible_palindrome = i * j
            if is_palindrome(possible_palindrome) and possible_palindrome > palindrome:
                palindrome = possible_palindrome
            j -= 1
        i -= 1

    return palindrome


if __name__ == "__main__":
    print(find_palindrome())