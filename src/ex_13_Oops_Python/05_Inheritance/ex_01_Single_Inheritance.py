# Single Inheritance
# A subclass/child/son inherits from one Parent/Base/Father.

class BaseTest:
    driver = "chromedriver"
    __driver2 ="FF"

    def setup(self):
        print("Based setup with the browser and env"+self.__driver2)

class LoginTest(BaseTest):
    def run(self):
        self.setup()
        print("Running the Testcases -> " + self.driver)


t  =LoginTest()
t.run()