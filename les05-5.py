with open('new05-5.txt', "w+") as f:
    numbers = input('Введите числа через пробел: ')
    f.write(numbers)

    f.seek(0)
    text = f.read()
    numbers_list = list(map(int, text.split()))
    print(sum(numbers_list))
