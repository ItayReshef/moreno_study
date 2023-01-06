import math
def is_prime(number: int)-> bool:

subject = 600851475143
solution = 9
answer = 0
is_primal = True
primal_checker = 0
while solution < subject:
    primal_checker = solution - 1
    while primal_checker > 1:
        if solution % primal_checker == 0:
            is_primal = False
            break
        primal_checker -= 1
    if is_primal:
        answer = solution
    is_primal = True
    solution += 1
print(answer)