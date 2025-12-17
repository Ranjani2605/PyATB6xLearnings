import pytest
import requests
import allure


base_url = "https://restful-booker.herokuapp.com"
headers = {"Content-Type": "application/json"}

def get_token():
    base_path = "/auth"

    full_url = base_url + base_path
    json_data = {
        "username" : "admin",
        "password" : "password"
    }

    response_data = requests.post(url = full_url, headers= headers, json = json_data)
    print(response_data)

    assert response_data.status_code == 200
    response_data_json = response_data.json()
    token = response_data_json["token"]
    print(token)

    assert isinstance(token, (str ,int))
    assert token > 0
    return token

def get_booking_id():
    base_path = "/booking"
    full_url = base_url + base_path
    json_payload = {
        "firstname": "Amit",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }

    response_data = requests.post(url = full_url, headers= headers, json = json_payload)
    response_data_json = response_data.json()
    booking_id = response_data_json["booking_id"]
    return booking_id

def test_put():
    token = get_token()
    booking_id = get_booking_id()
    base_path = "/booking" + str(booking_id)
    full_url = base_url + base_path
    cookie = 'token = ' + token
    headers = {"Content-Type": "application/json", "Cookie": cookie}

    json_payload = {
        "firstname": "Pramod",
        "lastname": "Brown",
        "totalprice": 111,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2018-01-01",
            "checkout": "2019-01-01"
        },
        "additionalneeds": "Breakfast"
    }
    response_data = requests.put(url = full_url, headers= headers, json = json_payload)
    assert response_data.status_code == 200
    assert response_data.json()['firstname'] == 'Pramod'

def test_delete():
    url = "https://restful-booker.herokuapp.com/booking/"
    booking_id = get_booking_id()
    Delete_url = url + str(booking_id)
    cookie_value = "token=" + get_token()
    headers = {"Content-Type": "application/json", "Cookie": cookie_value}
    response = requests.delete(url = Delete_url, headers= headers)
    assert response.status_code == 201
