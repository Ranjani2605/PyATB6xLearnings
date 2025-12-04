def before_after_ui_test(func):
    def wrapper():
        print("Before running UI Code")
        func()
        print("After Running UI code")
    return wrapper()

@before_after_ui_test
def test_ui():
    print("Hi, I am testing a UI Test")