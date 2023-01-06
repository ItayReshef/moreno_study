import math
TARGET_NUMBER = 13195

def largest_prime_factor(subject: int)-> int:
    minimal_possible_answer = round(subject / 2)
    multiplier = minimal_possible_answer
    for y in reversed(range(minimal_possible_answer)):

        for y in reversed(range(minimal_possible_answer)):
            if minimal_possible_answer * multiplier == subject and is_prime(minimal_possible_answer):
                return minimal_possible_answer
            multiplier -= 1
        minimal_possible_answer -= 1
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



# subject = 600851475143
# solution = 9
# answer = 0
# is_primal = True
# primal_checker = 0
# while solution < subject:
#     primal_checker = solution - 1
#     while primal_checker > 1:
#         if solution % primal_checker == 0:
#             is_primal = False
#             break
#         primal_checker -= 1
#     if is_primal:
#         answer = solution
#     is_primal = True
#     solution += 1
# print(answer)