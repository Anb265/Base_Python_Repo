total_number = 0

def list_sum(numbers_list):
    global total_number
    for num in numbers_list:
        try:
            total_number += int(num)
        except ValueError:
            print("Сумма введенных чисел:", total_number)
            print('Введен не числовой символ. Выход из программы')
            return 'Exit'
    print("Сумма введенных чисел:", total_number)

while True:
    numbers = (input('Введите числа через пробел: '))  # строка
    numbers_list = numbers.split()
    if list_sum(numbers_list) == 'Exit':
        break
