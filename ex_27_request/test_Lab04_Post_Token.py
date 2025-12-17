import pytest
import requests
import allure

base_url = "https://restful-booker.herokuapp.com"
base_path = "/auth"
full_url = base_url + base_path

@pytest.mark.regression
def test_create_token():
    headers = {"content-Type": "application/json"}
    json_payload = {
        "username" : "admin",
        "password" : "password123"
    }
    response_data = requests.post(url = full_url, headers = headers, json = json_payload)
    print(response_data)

    assert response_data.status_code == 200
    response_data_json = response_data.json()
    token = response_data_json["token"]
    print(token)
    #assert type(token) == str
    assert isinstance(token, str)
    assert len(token) > 0




