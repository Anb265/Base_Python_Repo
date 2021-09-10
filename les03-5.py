numbers = int(input('Введите числа через пробел: ')) # строка
numbers_list = list(map(int, numbers.split( ))) # список из чисел
#num_sum = sum(numbers_list)
#
# for number in numbers:
#     if number.isdigit:
#         return int(number)

def sum(x):
    num_sum = sum(x)
    print(num_sum)

for i in numbers_list:
    sum(i)

sum(numbers_list)


