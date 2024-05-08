
def test_loginCorrect(client):
    response = client.post('/api/accountManager/login',
            json={
                "user": "chuky2101",
                "password": "195418Teby"
                }
            )
    assert b"success" in response.data

def test_loginIncorrect(client):
    cuentas=[["a","asd"],["a","asd"],[0,1]]
    for a in cuentas:
        response = client.post('/api/accountManager/login',
            json={"user": a[0],"password": a[1]})
    assert b"error" in response.data