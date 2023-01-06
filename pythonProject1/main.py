import math
#def is_prime(number: int):


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





#maxval = 1
#fibonacci = [1, 2]
#result = 0
#while fibonacci[len(fibonacci) - 1] < 4000000:
#    fibonacci.append(fibonacci[maxval-1]+fibonacci[maxval])
#    maxval = maxval+1
#for y in fibonacci:
#    if y%2 == 0:
#        result += y
#print(result)
