from time import sleep
from itertools import cycle

class TrafficLight:

    def __init__(self, color):
        self.__color = color


    def running(self):
        lights_list = ['красный', 'желтый', 'зеленый', 'желтый', 'красный', 'желтый']
        ind = lights_list.index(self.__color)
        lights = lights_list[ind:ind + 4]       # Это чтобы начиналось с цвета, заданного в объекте

        counter = 0                             # Для выхода из цикла
        for light in cycle(lights):

            if light == 'красный':
                for i in range(7, -1, -1):
                    print(f'\r{light} {i} c', end='')
                    sleep(1)
                print('')

            if light == 'желтый':
                for i in range(2, -1, -1):
                    print(f'\r{light} {i} c', end='')
                    sleep(1)
                print('')

            if light == 'зеленый':
                for i in range(10, -1, -1):
                    print(f'\r{light} {i} c', end='')
                    sleep(1)
                print('')

            counter += 1
            if counter == 10:
                break


t = TrafficLight('зеленый')
t.running()