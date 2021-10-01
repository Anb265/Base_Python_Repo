class ZeroDivision(Exception):
    def __init__(self, txt):
        self.txt = txt

def division(a, b):
    try:
        if b == 0:
            raise ZeroDivision('На ноль делить нельзя')
        else:
            print(a/b)
    except ZeroDivision:
        print('На ноль делить нельзя')

division(4, 0)
