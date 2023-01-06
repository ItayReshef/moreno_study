RANGE_START = 100
RANGE_END = 1000


def largest_palindrome():
    palindromes: list = []
    for first_number in reversed(range(RANGE_START, RANGE_END)):
        for second_number in reversed(range(RANGE_START, RANGE_END)):
            possible_palindrome = first_number * second_number
            if is_palindrome(possible_palindrome):
                palindromes.append(possible_palindrome)
    return max(palindromes)


def is_palindrome(number: int) -> bool:
    reversed_number = str(number)[::-1]  # reverses the string
    if str(number) == reversed_number:
        return True
    else:
        return False
