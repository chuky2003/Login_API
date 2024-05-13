import os
from time import sleep, time
from tokenize import String
from urllib import response
import pytest
from dotenv import load_dotenv

load_dotenv()

env=os.getenv

@pytest.mark.parametrize("user, password", [
    ("a", "password"),  # Correct username, incorrect password
    (0, 1)              # Invalid inputs
])
def test_login_incorrect(client, user, password):
    response = client.post('/api/accountManager/login',
                           json={"user": user, "password": password})
    assert b"error" in response.data

@pytest.mark.parametrize("user, password", [
    ("chuky2101", "195418Teby")
])
def test_login_correct(client, user, password):
    response = client.post('/api/accountManager/login',
                           json={"user": user, "password": password})
    assert b"success" in response.data
    token = response.json.get("success", {}).get("token")
    assert token is not None

def test_refresh_token(client):
    login_response = client.post('/api/accountManager/login',
                                 json={"user": "chuky2101", "password": "195418Teby"})
    assert b"success" in login_response.data
    token = login_response.json.get("success", {}).get("token")
    assert token is not None

    refresh_response = client.post('/api/authToken/refreshToken', headers={'Authorization': token})
    assert b"token" in refresh_response.data
    refreshed_token = refresh_response.json.get("token")
    assert refreshed_token is not None

#!!!!la siguente funcion realentiza la aplicacion durante 60 segundos-
# ya que es para verificar su utilizacion

def test_endpoint_with_refreshed_token(client):
        pass
#       #login
#       login_response = client.post('/api/accountManager/login',
#                                    json={"user": "chuky2101", "password": "195418Teby"})
#       token = login_response.json["success"]["token"]
#       #refresh
#       duration=int(env("TOKEN_DURATION"))
#       sleep((duration*60)-1)
#       refresh_response = client.post('/api/authToken/refreshToken', headers={'Authorization': token})
#       refreshedToken=refresh_response.json["token"]
#       #test
#       test_response = client.post('/api/authToken/test', headers={'Authorization': refreshedToken})
#       assert b"success" in test_response.data
