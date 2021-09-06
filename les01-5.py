revenue = int(input('Введите выручку фирмы: '))
costs = int(input('Введите издержки фирмы: '))

profit = revenue - costs

if profit > 0:
    print('Фирма отработала с прибылью')
    efficiency = profit/revenue
    print(f'Рентабельность фирмы: {efficiency:.2}')
    staff = int(input('Введите численость сотрудников фирмы: '))
    profit_per_staff = profit / staff
    print(f'Прибыль фирмы в расчете на одного сотрудника: {profit_per_staff}')
else:
    print('Работа фирмы не принесла прибыли')