
import bcrypt
from dotenv import load_dotenv,dotenv_values
import os
import jwt
import datetime
from flask import request,Blueprint,abort
from sqlalchemy import true
from utils.queryManager import queryGetRows
from functools import wraps
from utils.customsExceptions import *

load_dotenv()

env=os.getenv

SECRET_KEY=env("SECRET_KEY")

def createToken(content,secret_key,duration):
    payload={}
    payload.update(content)
    payload.update({'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=duration)})
    token = jwt.encode(payload, secret_key, algorithm='HS256')
    return token

#-------------------------------------------------------------------------------------------
#-------------------------VALIDACION DE AUTORIZACION JWT------------------------------------
#-------------------------------------------------------------------------------------------

async def check_auth_middleware():
    login_token = request.headers.get('Authorization')
    if (not login_token):
            abort(403)
    inList=await queryGetRows("select token from ZF_BLACKLIST where token=%s",(login_token,))
    if(len(inList)>=1):
        #return{"error":"token expirado"},401 
        abort(403)
    try:
        resultado=jwt.decode(login_token, SECRET_KEY, algorithms="HS256")
        result={"id":resultado["userID"],"role":resultado["role"]}
        return result
    except:
        abort(403)
        #return{"error":"token incorrecto"},401

def checkAuth(f):
    @wraps(f)
    async def decorated_function(*args, **kwargs):
        result=await check_auth_middleware()  # Aplica el middleware de autorización
        return await f(*args,*kwargs,result)

    return decorated_function

request_counts = {}
request_wait_times = {}

class exceptionsAuth(ValueError):
        class password(ValueError):
             pass
        class onListOfAwait(ValueError):
             pass


async def authOfPass(password,passHashed,userID,role):
        if bcrypt.checkpw(password.encode("utf-8"), passHashed.encode('utf-8')):
                token=createToken({'userID':userID, 'role':role},SECRET_KEY,60)
                return token
        else:
            raise incorrect.Password