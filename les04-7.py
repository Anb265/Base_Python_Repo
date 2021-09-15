from math import factorial

def fact(n):
    for i in range(1,n+1):
        factor = factorial(i)
        yield (f'{i}! = {factor}')


n = int(input('Введите число: '))
for el in fact(n):
    print(el)