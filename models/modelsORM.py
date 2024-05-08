import code
import email
import bcrypt
from flask import session
from flask_sqlalchemy import SQLAlchemy
import pymysql
import sqlalchemy as sa
from sqlalchemy import text
from datetime import datetime
from sqlalchemy import false
from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import UniqueConstraint
from typing import Optional

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "ZF_ACCOUNTS"
    _id = db.Column(db.Integer(), primary_key=True, unique=True)
    user = db.Column(db.String(70), nullable=False, unique=True)
    email = db.Column(db.String(320), nullable=False, unique=True)
    password = db.Column(db.String(70), nullable=False)
    code = db.Column(db.Integer())
    expCode = db.Column(db.DateTime())
    role= db.Column(db.Integer(),default={0})

    @classmethod
    def selectUserByName(cls,userName=None)-> Optional['User']:
        return (cls.query.filter_by(user=userName).first())
    
    
    @classmethod
    def selectUserByEmail(cls,email=None)-> Optional['User']:
        return (cls.query.filter_by(email=email).first())
    
    @classmethod
    def createAccount(cls,email=None,userName=None,password=None):
        db.session.add(User(email=email,user=userName,password=password))
        db.session.commit()

    @classmethod
    def refreshRecoveryCode(cls,code,codeExp,email):
        cls.query.filter_by(email=email).update({
            User.code:code,
            User.expCode:codeExp
        })
        db.session.commit()

    @classmethod
    def changePass(cls,password,emailField):
        # Hash the new password
        password_bytes = password.encode('utf-8')
        password_hashed = bcrypt.hashpw(password_bytes, bcrypt.gensalt(13))
        password_hashed_str = password_hashed.decode('utf-8')
        #user_to_update = cls.query.filter_by(email=emailField).first()
        cls.query.filter_by(email=emailField).update({
            User.code:None,
            User.password:password_hashed,
            User.expCode:None,
        })
        try:
            db.session.commit()
        except Exception as e:
            print("Error al actualizar la contraseña:", e)

    @classmethod
    async def verifyExistCode(cls,code):
        CodeInAccount = db.session.query(User).filter_by(code=code).first()
        db.session.commit()
        if(not CodeInAccount):
            return False
        return True

    @classmethod
    async def getCode(cls,code,email):
        hourNow=datetime.now()
        CodeInAccount = db.session.query(User).filter_by(email=email,code=code).first()
        db.session.commit()
        if(not CodeInAccount):
            return False
        if(CodeInAccount.expCode<hourNow):
            return False
        return True

class Posts(db.Model):
    __tablename__ = "ZF_POSTS"
    __table_args__ = {'sqlite_autoincrement': True}
    idPost = db.Column(db.Integer(), primary_key=True, unique=True, autoincrement=True)
    _idUser = db.Column(db.Integer(), nullable=False)
    html = db.Column(db.Text(), nullable=False)
    title =db.Column(db.String(130), nullable=False)
    lastModify = db.Column(db.DateTime(), nullable=False)
    createDate = db.Column(db.DateTime(), nullable=False)
    public = db.Column(db.Boolean, nullable=False)
    thanks= db.Column(db.Integer(),server_default='0')
    
class blackList(db.Model):
    __tablename__ = "ZF_BLACKLIST"
    _id = db.Column(db.Integer(), primary_key=True)
    token = db.Column(db.String(122), nullable=False, unique=True)


class blackListCode(db.Model):
    __tablename__ = "ZF_BLACKLIST_CODE"
    _id = db.Column(db.Integer(), primary_key=True)
    codeExpired = db.Column(db.Integer())

class tags(db.Model):
    __tablename__="ZF_TAGS"
    _id = db.Column(db.INTEGER(), primary_key=True, autoincrement=True)
    name = db.Column(db.String(30), nullable=False)

class tags_posts(db.Model):
    __tablename__="ZF_TAGS_POSTS"
    _id = db.Column(db.Integer(), primary_key=True)
    _idPost=db.Column(db.INTEGER(),db.ForeignKey('ZF_POSTS.idPost'),nullable=False)
    _idTag=db.Column(db.INTEGER(),db.ForeignKey('ZF_TAGS._id'),nullable=False)
    #__table_args__ = (UniqueConstraint('_idPost', '_idTag', name='_idPost_idTag_uc'), )

#PRIMARY KEY (post_id, tag_id),
#FOREIGN KEY (post_id) REFERENCES posts(post_id),
#FOREIGN KEY (tag_id) REFERENCES tags(tag_id)
    #head=db.Column(db.INTEGER(),server_default='0')

#class relationAccountsPosts(db.Model):
#    __tablename__="ZF_POSTSSECTIONS"
#    idRelation= db.Column(db.Integer(),primary_key=True)
    #idUser = db.Column(db.Integer(), db.ForeignKey('ZF_ACCOUNTS._id'), nullable=False)
    #idPosted = db.Column(db.Integer(), db.ForeignKey('ZF_POSTS.idPost'), nullable=False)
    #FOREIGN KEY (idPost) REFERENCES ZF_POSTS(idPost),
    #FOREIGN KEY (_id) REFERENCES ZF_ACCOUNTS(_id)
    

