with open('new05-2.txt', 'r') as f:
    lines = f.readlines()
    print('Количество строк в файле:', len(lines))
    for i in range(0, len(lines)):
        print(f'Количество слов в строке {i+1}: {len(lines[i].split())}')