
import os
from dotenv import load_dotenv,dotenv_values
import pymysql

load_dotenv()

env=os.getenv

import mysql.connector

cnx = pymysql.connect(host=env("HOST_DB"),
                             user=env("USER_DB"),
                             password=env("PASSWORD_DB"),
                             database=env("DATABASE_DB"),
                             charset='utf8mb4',)


async def queryInsert(string,data):
    cnx.ping()
    result=cnx.cursor()
    result.execute(string,data)
    cnx.commit()

async def queryInsertWithReturnID(string,data):
    cnx.ping()
    result=cnx.cursor()
    result.execute(string,data)
    id=result.lastrowid
    cnx.commit()
    return id
    

async def queryDelete(string,data):
    cnx.ping()
    result=cnx.cursor()
    result.execute(string,data)
    resultado=result.rowcount
    cnx.commit()
    return resultado
    

async def queryGetRows(string,data):
        cnx.ping()
        result=cnx.cursor()
        result.execute(string,data)
        resultado=result.fetchall()
        cnx.close()
        return resultado

def queryUpdate(string,data):
    cnx.ping()
    cursor=cnx.cursor()
    cursor.execute(string,data)
    cnx.commit()
