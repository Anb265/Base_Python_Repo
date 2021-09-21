my_dict = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}

with open('new05-4.txt', 'r') as f:
    new_list = []
    for line in f:
        for i in my_dict:
            if i in line:
                new_line = line.replace(i, my_dict[i])
                new_list.append(new_line)
    print(new_list)

with open('new_file05-4.txt', 'w', encoding='utf-8') as new_f:
    for i in new_list:
        new_f.write(i)



