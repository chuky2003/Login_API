import pytest

def test_create_account(client, user="test2021", password="123456Test", email="test2021@hotmail.com"):
    """Verifica si un usuario ya existe en la base de datos."""
    response = client.post('/api/accountManager/register', json={
        "user": user,
        "email": email,
        "password": password
    })
    assert b"success" in response.data

def test_create_user_already_exist(client, user="test2021", password="123456Test", email="test2021@hotmail.com"):
    """Verifica si un usuario ya existe en la base de datos."""
    client.post('/api/accountManager/register', json={
        "user": user,
        "email": email,
        "password": password
    })
    response = client.post('/api/accountManager/register', json={
        "user": user,
        "email": email,
        "password": password
    })
    assert b"error" in response.data
    assert b"el usuario ingresado corresponde a una cuenta existente" in response.data 
