# test_app.py
import pytest
from time import sleep

def test_login_correct(client, user="test2005", password="123456Test",email="teste1@hotmail.com"):
    client.post('/api/accountManager/register', json={
        "user": user,
        "email": email,
        "password": password
    })
    # print(response.json)
    response1 = client.post('/api/accountManager/login',
                           json={"user": user,"password":password})
    assert b"success" in response1.data
    token = response1.json.get("success", {}).get("token")
    assert token is not None


def test_user_incorrect(client, user="UsuarioIncorrect", password="Messias."):
    response = client.post('/api/accountManager/login',
                           json={"user": user, "password": password})
    assert b"error" in response.data
    assert b"el usuario ingresado" in response.data

def test_parameters_invalid(client):
    response =client.post('/api/accountManager/login',
                        json={"user":15,"password":16})
    assert b"error" in response.data
    assert b"el usuario debe tener entre"


# !!!!la siguente funcion realentiza la aplicacion durante 60 segundos-
# ya que es para verificar su utilizacion

# @pytest.mark.parametrize("user, password", [
#     (user_test, password_test)
# ])
# def test_endpoint_with_refreshed_token(client,user,password):
#       #login
#       login_response = client.post('/api/accountManager/login',
#                                    json={"user": user, "password": password})
#       token = login_response.json["success"]["token"]
#       #refresh
#       duration=int(env("TOKEN_DURATION"))
#       sleep((duration*60)-6)
#       refresh_response = client.post('/api/authToken/refreshToken', headers={'Authorization': token})
#       refreshedToken=refresh_response.json["token"]
#       #test
#       test_response = client.post('/api/authToken/test', headers={'Authorization': refreshedToken})
#       assert b"success" in test_response.data
#
