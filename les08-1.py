from datetime import date


class Data:
    def __init__(self, input_data):
        self.input_data = input_data

    @classmethod
    def num(cls, input_data):
        data_list = list(map(int, input_data.split('-')))
        day, month, year = data_list[0], data_list[1], data_list[2]
        return day, month, year

    @staticmethod
    def valid(input_data):
        data_list = list(map(int, input_data.split('-')))
        try:
            input_date_reverse = date(data_list[2], data_list[1], data_list[0])
            today_data = date.today()
            if today_data < input_date_reverse:
                return ('Введенная дата еще не наступила')
            else:
                return (input_data)
        except ValueError:
            return('Неверный формат даты')


#d = Data('32-12-1998')
print(Data.num('30-12-1998'))
print(Data.valid('29-02-2020'))


# if data_list[1] < 0 or data_list[1] > 12:
#     return 'Введите корректный номер месяца'
# else:
#     if data_list[0] < 0 or data_list[0] > 31:
#         return 'Введите корректное число'
#     else:
#         if data_list[2] < 0 or data_list[2] > 2021:
#             return 'Введите корректный год'
#         else:
#             return(input_data)
