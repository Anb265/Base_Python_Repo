string = input('Введите элементы списка через пробел: ')
new_list = string.split( )

i = 0
if len(new_list) // 2 == 1:
    new_list_last = new_list.pop()
    while i < len(new_list):
        new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]
        i += 2
    new_list.append(new_list_last)
else:
    while i < len(new_list):
        new_list[i], new_list[i + 1] = new_list[i + 1], new_list[i]
        i += 2

print(new_list)



