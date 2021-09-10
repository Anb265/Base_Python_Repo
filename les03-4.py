# Первое решение:
# def my_func(x,y):
#     result = x ** y
#     print(result)

#Второе решение:

def my_func(x, y):
    i = 0
    t = 1
    while i < abs(y):
        t = t * x
        i += 1
    result = 1/t
    print(result)

x = float(input('Введите целое положительное число: '))
y = int(input('Введите целое отрицательное число: '))

my_func(x, y)