class TestExample:

    def __init__(self):
        self.driver = 'chrome'
        self._config = 'stage'
        self.__api__key = 'ABCDEFG'


    def show(self):
        print('Public:',self.driver)
        print('Protect:' ,self._config)
        print('api:',self.__api__key)


object = TestExample()

object.show()
print(object.driver) # allowed
print(object._config) # allowed but good pratice
print(object.__api__key) # not allowed