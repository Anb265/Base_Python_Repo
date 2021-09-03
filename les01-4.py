number = list(input('Введите число: '))
int_number = [int(x) for x in number]
max_num = 1
i = len(int_number)

print(i)
while i > 0:
    i -= 1

    while max_num < int_number[i]:
        max_num = int_number[i]

print(max_num)

