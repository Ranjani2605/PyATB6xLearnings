class BaseTest:
    def run(self):
        print("Running generic test")

class LoginTest(BaseTest):

    def run(self):
        print("Running Login test")


obj_logintest = LoginTest()
obj_logintest.run()
obj_basetest = BaseTest()
obj_basetest.run()