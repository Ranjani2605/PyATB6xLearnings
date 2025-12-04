class BaseClass():
    def __init__(self):
        self._driver = 'Chrome'


    def setup(self):
        print('Launching browser:', self._driver)

    def teardown(self):
        print('closing browser')

class LoginTest(BaseClass):

    def __init__(self, username, password):
        super().__init__()
        self.__username = username
        self.__password = password

    def get_user(self):
        return self.__username

    def run_test(self):
        print('Running login test with username:', self.get_user())

login = LoginTest('admin', '11314')
login.setup()
login.run_test()
login.teardown()