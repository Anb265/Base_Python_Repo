class NotInt(Exception):
    def __init__(self, txt):
        self.txt = txt


def InputNum():
    full_list = []
    while True:
        print('Для выхода введите "stop": ')
        num_list = input('Введите числа через пробел: ')
        new_list = num_list.split( )
        if num_list == 'stop':
            break
        else:
            for i in new_list:
                try:
                    if i.isdigit() == False:
                        raise NotInt('Введено не число')
                    else:
                        full_list.append(int(i))
                except NotInt:
                    print(f'Введено не число - {i}')
    print(full_list)

InputNum()