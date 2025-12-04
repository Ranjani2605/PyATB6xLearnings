from dotenv import load_dotenv
import os


class Login:

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def validate_login_page(self):
        load_dotenv()
        if self.email == os.getenv("Username") and self.password == os.getenv("Password"):
            print('Login successful')
        else:
            print('Login failed')

email = input('Enter your email: ')
password = input('Enter your password: ')

login = Login(email, password)
login.validate_login_page()
