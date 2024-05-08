from flask import Blueprint,request
import jwt
from utils.queryManager import queryInsert

logOutApp=Blueprint('logOut',__name__)

@logOutApp.put('/logOut')
async def logOut():
    authorization=request.headers.get("authorization")
    if(not authorization):
        return{"error":"parametros incorrectos"},400
    try:
        await queryInsert("insert into ZF_BLACKLIST(token) values (%s)",(authorization,))
        return{"sucessfully":"desconectado correctamente"}
    except:
        return{"error":"el token indicado ya está desconectado"},401
    