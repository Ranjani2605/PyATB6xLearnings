# Multiple Inheritance

"""
A class inherits from more than one parents class
if the Parent classes have the same name.

what is MRO (Method Resolution Order) in Python
MRO stands for Method Resolution order.
It is the order in which Python searches for a method or attribute when multiple
inheritance is used. It defines which parent class method is called first.
"""


class Father1:
    def money(self):
        print('Father1 Money')


class Father2:
    def money(self):
        print('Father2 Money')


class child(Father2, Father1):
    def give_money(self):
        print('Child Money')
        self.money()

obj = child()
obj.give_money()
