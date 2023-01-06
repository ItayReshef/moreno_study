from math import sqrt

SMALLEST_NON_PRIME_INTEGER = 2


def is_prime(number: int) -> bool:
    for denominator in range(SMALLEST_NON_PRIME_INTEGER, round(sqrt(number))):
        if number % denominator == 0:
            return False
    return True


def largest_prime_factor(number: int):
    for factor in reversed(range(SMALLEST_NON_PRIME_INTEGER, round(sqrt(number)))):
        if number % factor == 0 and is_prime(factor):
            return factor
    return True
