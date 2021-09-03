number = list(input('Введите число: '))
int_number = [int(x) for x in number]
max_num = 0
i = 0

print(i)
while max_num < int_number[i]:
    i+=1
    max_num = int_number[i]

print(max_num)


