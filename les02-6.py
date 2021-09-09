goods = []
char = ('название', 'цена', 'количество', 'ед')
num = 1

while True:
    print('1. Ввести данные\n2. Вывести данные\n3. Выход')
    choice = input('Выберите пункт меню - ')
    if choice == '1':
        item_char = {}
        item = (num, item_char)
        for i in char:
            item_char[i] = input(f'Введите значение поля {i}: ')
        goods.append(item)
        num +=1

    elif choice == '2':
        for item in goods:
            print(item)

        # new_dict = {}
        #
        # for x, y in item_char.items():
        #     all_char = [y]
        #     new_dict[x] = all_char
        #     for item in goods:
        #         all_char.append(y)
        #
        # print(new_dict)

    elif choice == '3':
        break
    else:
        print('Выберите корректный пункт меню')


