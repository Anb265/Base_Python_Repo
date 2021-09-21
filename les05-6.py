def digits_in_string(string):
    num = ''
    for i in string:
        if i.isdigit():
            num += i
    if len(num) != 0:
        return int(num)
    else:
        return 0


with open('new05-6.txt', 'r', encoding='utf-8') as f:
    new_dict = {}
    for line in f:
        new_line = line.split( )
        subject_hours = []
        for i in new_line:
            a = digits_in_string(i)
            subject_hours.append(a)
            sum_hours = sum(subject_hours)
            new_dict[new_line[0]] = sum_hours
    print(new_dict)