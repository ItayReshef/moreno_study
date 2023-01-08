import math
TARGET_NUMBER = 600851475143

def largest_prime_factor(subject: int)-> int:
    minimal_possible_answer = round(math.sqrt(subject))
    for j in reversed(range(minimal_possible_answer)):
        if (subject % j  == 0 and is_prime(j)):
            return j
    return 0


def is_prime(number: int)-> bool:
    is_primal = True
    primal_checker = number - 1
    while primal_checker > 1:
        if number % primal_checker == 0:
            is_primal = False
            break
        primal_checker -= 1
    if is_primal:
        return True
    else:
        return False


print(largest_prime_factor(TARGET_NUMBER))
