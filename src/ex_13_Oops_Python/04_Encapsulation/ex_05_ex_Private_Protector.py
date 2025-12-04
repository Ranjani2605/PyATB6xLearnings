from webbrowser import Chrome


class TestExample:
    def __init__(self):
        self.public = 'Public'
        self.__private = 'Private'
        self._protect = 'Protected'

    def __chrome(self): # private method
        print('omg it is worked')

    def method(self): # public method
        print("Hello World")
        self.__chrome()



object = TestExample()
object.method()

print(object._protect)# Technically accessible, but not recommended

