class Cell:
    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        cell_sum = self.quantity + other.quantity
        return f'Сумма ячеек двух клеток: {cell_sum}'

    def __sub__(self, other):
        if self.quantity - other.quantity != 0:
            cell_sub = abs(self.quantity-other.quantity)
            return f'Разность ячеек двух клеток: {cell_sub}'
        else:
            return 'Разность ячеек двух клеток равна 0'

    def __mul__(self, other):
        cell_mul = self.quantity *other.quantity
        return f'Произведение ячеек двух клеток: {cell_mul}'

    def __truediv__(self, other):
        cell_truediv = round(self.quantity / other.quantity)
        return f'Целочисленное деление ячеек двух клеток: {cell_truediv}'

    def make_order(self, mesh_in_row):
         for i in range(0,self.quantity // mesh_in_row):
             print('*'*mesh_in_row)
         print('*'*(self.quantity % mesh_in_row))


c1 = Cell(5)
c2 = Cell(10)

print(c2+c1)
print(c2-c1)
print(c2*c1)
print(c2/c1)
c2.make_order(3)
c1.make_order(8)