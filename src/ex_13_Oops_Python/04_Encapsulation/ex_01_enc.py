class Car:


 # 1st options but best pratice
    name = None
    make = None     # This is called instant variable
    model = None

    def __init__(self, o_name, o_make, o_model):
        self.name = o_name
        self.make = o_make
        self.model = o_model


# 2nd options

    def __init__(self, name, make, model):
        self.name = name
        self.make = make
        self.model = model