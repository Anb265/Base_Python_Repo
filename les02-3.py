dict = {'зима':(1, 2, 12), 'весна':(3, 4, 5), 'лето':(6, 7, 8), 'осень':(9, 10, 11)}
month = int(input('Введите номер месяца: '))
if month > 0 and month < 12:
    for season, month_num in dict.items():
        if month in month_num:
            print(season)
       # else:
       #     pass

else:
    print('Ты помнишь, что у нас 12 месяцев?')