class Person:

    def __init__(self, first_name, last_name, age, height, weight):

        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.height = height
        self.weight = weight

    def display_first_name(self):
        print(f"Person first name is:", self.first_name)

    def display_last_name(self):
        print(f"Person last name is:",self.last_name)

    def display_age(self):
        print(f"Person age is:",self.age)

    def display_height(self):
        print(f"Person height is:", self.height)

    def display_weight(self):
        print(f"Person weight is:", self.weight)

obj_person = Person("Ram", "Kumar",25, 5.9, 78)
obj_person.display_first_name()
obj_person.display_last_name()
obj_person.display_age()
obj_person.display_weight()
obj_person.display_height()