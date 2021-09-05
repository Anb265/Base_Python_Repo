number = input('Введите число: ')
max_num = 0

for j in number:
        i=int(j)
        while max_num < i:
                max_num = i
                
print(max_num)
