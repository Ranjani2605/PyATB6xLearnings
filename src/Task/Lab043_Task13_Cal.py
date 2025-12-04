class Calculator:

    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2


    def sum(self):
        return self.num1 + self.num2

    def multiple(self):
        return self.num1 * self.num2


obj_cal = Calculator(20,50)
print(obj_cal.sum())
print(obj_cal.multiple())

