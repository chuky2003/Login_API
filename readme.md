
# Forum

## Installation and running

```bash
  cd backEnd
  virtualenv env
  .\env\Script\activate
  pip install --upgrade -r "requirements.txt"
  flask --app server.py run --reload
```
    
## API Reference
#### Host default: https://localhost:5000

#### Creation of account

```http
  POST /api/accountManager/register
```
##### JSON
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `user   ` | `string` | **Required**. Your API key |
| `pass   ` | `string` | **Required**. Your API key |
| `email  ` | `string` | **Required**. Your API key |

#### LogIn of account
```http
  GET /api/accountManager/login
```
##### JSON
| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `user   ` | `string` | **Required**. Your API key |
| `pass   ` | `string` | **Required**. Your API key |

#### LogOut of account
```http
  PUT /api/authManager/logOut
```
##### Header
| Parameter         | Type     | Description                |
| :---------------- | :------- | :------------------------- |
| `Authorization  ` | `string` | **Required**. Your API key |

#### Test token
```http
  GET /api/accountManager/token
```
##### Header
| Parameter         | Type     | Description                |
| :---------------- | :------- | :------------------------- |
| `Authorization  ` | `string` | **Required**. Your API key |




