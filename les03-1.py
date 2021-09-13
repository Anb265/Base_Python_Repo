def division(a, b):
    result = a / b
    print(result)

a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))

if b == 0:
    print('На ноль делить нельзя')
else:
    division(a, b)
