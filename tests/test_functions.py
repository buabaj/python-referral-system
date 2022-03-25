from http import client
from fastapi.testclient import TestClient
from app import app


client = TestClient(app)

# test index route for 200 status code


def test_index_route():
    response = client.get("/")
    assert response.status_code == 200

# test register user route for 200 status code


def test_register_user_route():
    response = client.post("/register_user", json={
        "first_name": "jerry",
        "last_name": "buaba",
        "phone": "504782862",
        "email": "jerrytest@example.com",
        "token": "1234567890",
        "created_at": "2022-03-25T08:27:07.703Z",
        "updated_at": "2022-03-25T08:27:07.703Z"
    })
    assert response.status_code == 200

# test get referral code route for 200 status code


def test_get_referral_code_route():
    response = client.post("/get_referral_code", json={
        "email": "jerrytest@example.com"})
    assert response.status_code == 200
    code = response.json()
    return code

# test check referral code validity route for 200 status code


def test_check_referral_code_validity_route(code):
    response = client.post("/check_referral_code_validity", json={
        "referral_code": test_get_referral_code_route()})
    assert response.status_code == 200

# test redeem referral code route for 200 status code


def test_redeem_referral_code_route(code):
    response = client.post("/redeem_referral_code", json={
        "referral_code": test_get_referral_code_route()})
    assert response.status_code == 200
