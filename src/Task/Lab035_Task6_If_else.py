# Q 1 Api response code

api_responses = int(input("Api status code : ").strip())

if api_responses == 200:
    print("Passed API Request")
else:
    print("Failed API Request")

# Q2 In automation, you often compare expected and actual outputs.
# Write code to check if a test case passed or failed.

expected_title = str(input("Enter the title: "))
actual_title = "Dashboard"

if expected_title.strip().lower() == actual_title.strip().lower():
    print("Test Passed-Title matches")
else:
    print("Test failed- Title not matched")

# Q3 You want to check whether a web page loads within 3 seconds (performance test condition).
# load_time = 4.2
# ⚠️ Page load too slow: 4.2 seconds

page_load_time = float(input("web page loads").strip())

if page_load_time < 0:
    print('Invalid input! Load time cannot be negative')
else:
    if page_load_time  <= 3:
        print(f'Page loaded successfully in {page_load_time} seconds')
    else:
        print(f'Page load too slow : {page_load_time} seconds')

#Q4 Check if the user can log in based on correct username and password.

input_username = input("Enter username : ")
input_password = input("Enter password : ")
username = 'admin'
password = '12345'

if username == input_username and password == input_password:
    print('Login Successful')
else:
    print('Invalid Credentials')




