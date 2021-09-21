with open('new05-3.txt', 'r') as f:
    new_sum = 0
    employee_num = 0
    surnames = []
    for line in f:
        line = line.split(": ")
        if int(line[1]) < 20000:
            surnames.append(line[0])

        new_sum += int(line[1])
        employee_num += 1
    print('Сотрудники с окладом менее 20000: ', ', '.join(surnames))

    averege = new_sum/employee_num
    print('Средний оклад всех сотрудников:', averege)
