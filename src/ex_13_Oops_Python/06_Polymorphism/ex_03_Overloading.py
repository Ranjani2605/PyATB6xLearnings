# In python overloading is impossbile

class MathClass:

    def add(self, a , b):
        return a + b

    def add(self, a, b):
        return a + b


obj_math = MathClass()
print(obj_math.add(1, 2))
print(obj_math.add(1, 2))