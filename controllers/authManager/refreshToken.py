from dotenv import load_dotenv,dotenv_values
import os
import jwt
import datetime
from flask import Blueprint,request,Request
from utils.queryManager import queryGetRows
from utils.Auth import createToken

load_dotenv()

env=os.getenv

SECRET_KEY=env("SECRET_KEY")

refreshToken=Blueprint("token",__name__)

@refreshToken.post("/refreshToken")
async def tokenSession():
    login_token = request.headers.get('Authorization')
    if not login_token:
            return ({'message': 'No se proporcionó un token de sesión.'}), 401
    inList=await queryGetRows("select token from ZF_BLACKLIST where token=%s",(login_token,))
    if(len(inList)>=1):
        return{"error":"token expirado"},401 
    try:
        resultado=jwt.decode(login_token, SECRET_KEY, algorithms="HS256")
        del resultado['exp']
        token=createToken(resultado,SECRET_KEY,1)
        return {"token":token}
    except:
         return{"error":"token incorrecto"},401