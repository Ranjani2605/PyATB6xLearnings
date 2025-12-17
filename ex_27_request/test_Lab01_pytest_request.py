import allure
import pytest
import requests






@allure.title("TC#1-Verify the GET request.")
@allure.description("Verify that the GET request is basically successful and give you 200 OK as a status.")
@pytest.mark.positive
def test_get_request():
    url = "https://restful-booker.herokuapp.com/booking/1"
    response_data = requests.get(url)
    assert response_data.status_code == 200




@allure.title("Verify the GET Request of Restful Booker with invalid ID")
@allure.description("This Testcase check Booking -1 and verify the response")
@pytest.mark.negative
def test_get_request_negative():
    url_get = "https://restful-booker.herokuapp.com/booking/-1"
    response_data = requests.get(url_get)
    assert response_data.status_code == 404
