from flask import Flask, Blueprint,request
from utils.queryManager import *
import jwt
from dotenv import load_dotenv,dotenv_values
from flask import Blueprint, jsonify, request



load_dotenv()
env=os.getenv

SECRET_KEY=env("SECRET_KEY")

authToken=Blueprint('getData',__name__)

@authToken.post("/authToken")
async def tokenSession():
    from server import cache
    login_token = request.headers.get('Authorization')
    if not login_token:
            return ({'message': 'No se proporcionó un token de sesión.'}), 401
    #inList=await queryGetRows("select token from ZF_BLACKLIST where token=%s",(login_token,))
    #if(len(inList)>=1):
    #    return{"error":"token expirado"},401 
    cache_key = login_token
    result = cache.get(login_token)

    if result is None:
        try:
            result=jwt.decode(login_token, SECRET_KEY, algorithms="HS256")
            cache.set(cache_key, result, timeout=60)
            return {"result":result}
        except Exception as e:
             print(str(e))
             return{"error":"token incorrecto"},401
    return{"result":result}