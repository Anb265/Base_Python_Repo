from abc import ABC, abstractmethod

class QuantityError(Exception):
    def __init__(self, txt):
        self.txt = txt


class Warehouse:
    def __init__(self, equipment):
        self.total_quantity = equipment.total_count

    def ammount(self):
            return f'Всего техники на складе: {self.total_quantity}'

    def eq_acceptance(self, eq_dict):
        if type(eq_dict["quantity"]) != int:
            print (f'Введено неверное значение "quantity" для {eq_dict["name"]} подразделения {eq_dict["subdivision"]}')
        else:
            print(f'Количество {eq_dict["name"]} в подразделении {eq_dict["subdivision"]}: {eq_dict["quantity"]}')


class OfficeEquipment(ABC):
    total_count = 0
    def __init__(self, name, model, quantity, subdivision):
        self.eq_dict = {'name': name, 'model': model, 'quantity': quantity, 'subdivision': subdivision}
        try:
            if type(self.eq_dict['quantity']) != int:
                raise QuantityError('Неверный тип данных')
            else:
                OfficeEquipment.total_count += quantity
        except QuantityError:
            print(f'Допущена ошибка типа данных "quantity" = {quantity}')

    def acceptance(self, stock):
        stock.eq_acceptance(self.eq_dict)

    @abstractmethod
    def ammount():
        pass


class Printer(OfficeEquipment):
    printer_count = 0
    def __init__(self, name, model, quantity, subdivision, color):
        OfficeEquipment.__init__(self, name, model, quantity, subdivision)
        self.eq_dict['color'] = color
        if type(self.eq_dict['quantity']) == int:
            Printer.printer_count += quantity

    @staticmethod
    def ammount():
            print(f'Всего принтеров на складе: {Printer.printer_count}')

class Scanner(OfficeEquipment):
    scanner_count = 0
    def __init__(self, name, model, quantity, subdivision, resolution):
        OfficeEquipment.__init__(self, name, model, quantity, subdivision)
        self.eq_dict['resolution'] = resolution
        if type(self.eq_dict['quantity']) == int:
            Scanner.scanner_count += quantity

    @staticmethod
    def ammount():
            print(f'Всего сканеров на складе: {Scanner.scanner_count}')


class Copier(OfficeEquipment):
    copier_count = 0
    def __init__(self, name, model, quantity, subdivision, speed):
        OfficeEquipment.__init__(self, name, model, quantity, subdivision)
        self.eq_dict['speed'] = speed
        if type(self.eq_dict['quantity']) == int:
            Copier.copier_count += quantity

    @staticmethod
    def ammount():
            print(f'Всего ксероксов на складе: {Copier.copier_count}')


printer_1 = Printer('принтер', 'hp', '3', 'ПФО', 20)
printer_2 = Printer('принтер', 'hp', 8, 'Отдел кадров', 20)
scanner_1 = Scanner('сканер', 'hp', 'абракадабра', 'Бухгалтерия', 100)
scanner_2 = Scanner('сканер', 'hp', 2, 'Ресепшн', 100)
copier_1 = Copier('ксерокс', 'hp', 5, 'Бухгалтерия', 20)
copier_2 = Copier('ксерокс', 'hp', 8, 'Дирекция', 20)
w = Warehouse(OfficeEquipment)
print(w.ammount())

printer_1.acceptance(w)
printer_2.acceptance(w)
scanner_1.acceptance(w)
scanner_2.acceptance(w)
copier_1.acceptance(w)
copier_2.acceptance(w)

Printer.ammount()
Scanner.ammount()
Copier.ammount()

