from flask_mail import Mail,Message
from flask import Blueprint,request
from extension import mail


def enviar_correo(destinatary,asunto, message):

        # Crea un objeto Message para el correo electrónico
        msg = Message(asunto, recipients=[destinatary])
        msg.body = message
        # Envía el correo electrónico
        try:
            if(mail.connect()==True):
                mail.send(msg)
                return False
            return True
        except Exception as e:
            print(ValueError(e))
            return False
        