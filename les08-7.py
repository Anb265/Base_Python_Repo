class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        sum_result = self.a + other.a + (self.b + other.b)*1j
        return sum_result

    def __mul__(self, other):
        mul_result = (self.a * other.a - self.b * other.b) + (self.a * other.b + self.b * other. a)*1j
        return mul_result


num1 = ComplexNumber(1, 2)
num2 = ComplexNumber(3, 4)

print(num1+num2)
print(num1*num2)