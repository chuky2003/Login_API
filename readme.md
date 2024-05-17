
# login API
##### This is an backend login api ready from connect to your frontend

## Installation and running
```bash
  virtualenv env
  .\env\Script\activate
  pip install --upgrade -r "requirements.txt"
  flask --app server.py run --reload
```
    
## API Reference
#### Host default: https://localhost:5000

### Creation of account

| Parameters`JSON` | Description                |method|Url                        |
| :-------- | :------------------------- |:-----|:------------------------- |
| `user` `email` `password` | Create account |`POST`  |/api/accountManager/register|
| `user` `password`  | Return token if logged |`POST`  |/api/accountManager/login|
***

### Password recovery

| Parameters`JSON` | Description                |method|Url                        |
| :-------- | :------------------------- |:-----|:------------------------- |
| `email`| Send code to recovery Account|`POST`  |/api/accountManager/forgotAccount/sendCode|
| `email` `password` `code`  | Change password |`POST`  |/api/accountManager/forgotAccount/changePass|

### Management of token(JWT)
|parameters`HEADERS`| Description                           |Method | Url|
| :-------- | :------------------------- |:-----|:------------------------- |
|`Authorization`    | Testing token of Login or refreshToken|`POST` |/api/authToken/test|
|`Authorization`    | Refresh token(JWT) |`POST` |/api/authToken/refreshToken|
|`Authorization`    | Add actually token to blackList |`PUT` |/api/authToken/logOut|