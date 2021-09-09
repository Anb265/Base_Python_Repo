my_list = [7, 5, 3, 3, 2]
new_el = int(input('Введите число - новый элемент рейтинга: '))

x = len(my_list)

i = 0
while i < x-1:

    if new_el > my_list[0]:
        my_list.insert(0, new_el)
        print(my_list)
    elif new_el < my_list[-1]:
        my_list.append(new_el)
        print(my_list)
    elif new_el < my_list[i] and new_el >= my_list[i+1]:
        my_list.insert(i+1, new_el)
        print(my_list)
    i += 1




