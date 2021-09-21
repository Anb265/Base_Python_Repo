import json
with open('new05-7.txt', 'r', encoding='utf-8') as f:
    firms_with_profit = {}
    average_profit_dict = {}
    final_list = [firms_with_profit, average_profit_dict]
    sum_profit = 0
    i = 0
    for line in f:
        new_list = line.split( )
        profit = int(new_list[2]) - int(new_list[3])
        firms_with_profit[new_list[0]] = profit
        if profit > 0:
            sum_profit += profit
            i+=1
            average_profit = sum_profit/i
            average_profit_dict['average_profit'] = average_profit
    print(final_list)

with open('file05-7.json', 'w') as j_f:
    json.dump(final_list, j_f)