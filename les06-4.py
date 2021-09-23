class Car:
    def __init__(self, speed, color, name, is_police):
         self.speed = speed
         self.color = color
         self.name = name
         self.is_police = is_police

    def go(self):
        print(f'Автомобиль {self.name} начал движение')

    def stop(self):
        print(f'Автомобиль {self.name} остановился')

    def turn_left(self):
        print(f'Автомобиль {self.name} повернул налево')

    def turn_right(self):
        print(f'Автомобиль {self.name} повернул направо')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} - {self.speed} км/ч')


class TownCar(Car):
    def what_car(self):
        print(f'Это {self.name}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} - {self.speed} км/ч')
        if self.speed > 60:
            print(f'Автомобиль {self.name} превысил скорость на {abs(60-self.speed)} км/ч')


class SportCar(Car):
    def what_car(self):
        print(f'Это {self.name}')


class WorkCar(Car):
    def what_car(self):
        print(f'Это {self.name}')

    def show_speed(self):
        print(f'Текущая скорость автомобиля {self.name} - {self.speed} км/ч')
        if self.speed > 40:
            print(f'Автомобиль {self.name} превысил скорость на {abs(40-self.speed)} км/ч')


class PoliceCar(Car):
    def what_car(self):
        print(f'Это {self.name}')


town_car = TownCar(70, 'белый', 'Ford', False)
sport_car = SportCar(200, 'красный', 'Ferrari', False)
work_car = WorkCar(41, 'желтый', 'Taxi', False)
polic_car = PoliceCar(80, 'синий', 'Police', True)

print(town_car.name)
print(polic_car.is_police)

sport_car.go()
sport_car.show_speed()
sport_car.turn_right()
sport_car.turn_left()
sport_car.stop()
town_car.show_speed()
work_car.show_speed()