import requests
import pytest
import allure

base_url = "https://restful-booker.herokuapp.com"
base_path = "/booking"
full_url = base_url + base_path


@allure.title("TC#1 - Create Booking CRUD Positive")
@allure.description("Verify the create Booking!")
def test_create_booking_positive_tc1():

    headers = {
        "Content-Type": "application/json"
    }

    payload = {
        "firstname": "Jim",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response_data = requests.post(url = full_url, headers = headers, json = payload)
    assert response_data.status_code in [200, 201]

    response_json = response_data.json()
    print(response_json)

    booking_id = response_json["bookingid"]
    first_name = response_json["booking"]["firstname"]
    last_name = response_json["booking"]["lastname"]
    customer_name = first_name + " " + last_name
    print(customer_name)
    booking_checkin_date = response_json["booking"]["bookingdates"]["checkin"]
    booking_checkout_date = response_json["booking"]["bookingdates"]["checkout"]
    booking_date = booking_checkin_date + " " + booking_checkout_date
    print(booking_date)

    assert booking_id is not None
    assert booking_date > 0
    assert type(booking_date) == int


@allure.title("TC#2 - Create Booking CRUD Negative")
@allure.description("Verify that invalid payload Booking is not created!")
@pytest.mark.clurl
def test_create_booking_negative_tc1():
    header = {"Content-type" : "application/json"}
    json_payload = {}
    response = requests.post(url = full_url, headers = header, json = json_payload)
    assert response.status_code == 500
    assert response.text == "Internal Server Error"
