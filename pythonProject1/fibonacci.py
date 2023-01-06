maxval = 1
fibonacci = [1, 2]
result = 0
while fibonacci[len(fibonacci) - 1] < 4000000:
    fibonacci.append(fibonacci[maxval-1]+fibonacci[maxval])
    maxval = maxval+1
for y in fibonacci:
    if y%2 == 0:
        result += y
print(result)
