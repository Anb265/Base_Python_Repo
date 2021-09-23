class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def road_mass(self):
        full_mass = self._length * self._width * one_sq_m_mass * thickness
        return f'Масса асфальта, необходимая для покрытия всей дороги: {full_mass/1000} т'
a = int(input('Введите длину полотна дороги, м: '))
b = int(input('Введите ширину полотна дороги, м: '))
one_sq_m_mass = 25
thickness = 5

r = Road(a, b)
print(r.road_mass())

