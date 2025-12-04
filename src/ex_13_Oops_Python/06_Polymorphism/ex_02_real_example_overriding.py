class TestSuite:
    def info(self):
        print("Test suite information")

class BaseTest(TestSuite):
    def setup(self):
        print("Base setup")

    def run(self):
        print("Base test execution")

class LoginTest(BaseTest):
    def run(self):
        print("Login test execution")

class APITest(BaseTest):
    def run(self):
        print("API test execution")

obj_basetest = BaseTest()
obj_basetest.run()
obj_loginTest = LoginTest()
obj_loginTest.run()
obj_apiTest = APITest()
obj_apiTest.run()