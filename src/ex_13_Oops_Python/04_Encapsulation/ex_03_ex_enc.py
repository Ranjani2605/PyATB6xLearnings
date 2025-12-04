class Car:
    def __init__(self):
        self.public = 'public'
        self.__private = 'private'



    def get(self):
        return self.__private

car_object = Car()
print(car_object.public)
print(car_object.get())