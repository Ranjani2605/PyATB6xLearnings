import pytest
import allure


@allure.title("verify that the create booking, with invalid data is working.")
@allure.description("This Testcase check for the negative create booking.")
@pytest.mark.negative
def test_create_booking_negative():
    print("test_case#1")
    assert 1-1 == 2
@allure.title("verify that create booking, valid data is working")
@allure.description("We are going to verify that create booking in the future of this function.")
@pytest.mark.smoke
def test_create_booking_positive():
    print("test_case#2")
    assert 1+1 == 2

@allure.title("verify that create booking, Zero data is working")
@allure.description("verify that create booking, valid data is working")
@pytest.mark.postive
def test_create_booking_zero():
    print("test_case#3")
    assert 0 == 0

