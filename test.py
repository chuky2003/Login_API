
from typing import Optional
from  sqlalchemy import select
from models.modelsORM import User,db


# Ejemplo de cómo agregar un usuario a la base de datos desde cualquier parte de tu API
def agregar_usuario():
        nuevo_usuario = User(user='asd' ,email ="asd@hotmail.com",password="sadsdf")
        db.session.add(nuevo_usuario)
        db.session.commit()

def seleccionar_usuario():
        pass
       #usuario=User.selectUser(userName="asd")
       #print(usuario.email)
       #usu=User(usuario)
       #print(usu.code)
       #print(usuario)
       #print(usuarios)
       ##for usuario in usuarios:
       ##    print(f"ID: {usuario._}, Nombre de usuario: {usuario.user}, Correo electrónico: {usuario.email}")
       #return usuario
