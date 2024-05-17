from flask import Blueprint

# Crear una instancia de Blueprint



#---------------------------------------------
#---------------LOGIN REGISTER----------------
#---------------------------------------------
from controllers.accountManager.registerAccount import registerApp
from controllers.accountManager.loginAccount import loginAPP
from controllers.accountManager.forgotAccount import forgotAccount


prefixAccount = "/api/accountManager"
accountManager = Blueprint('accountManager', __name__,url_prefix=prefixAccount)

accountManager.register_blueprint(loginAPP)
accountManager.register_blueprint(registerApp)

#---------------------=FORGOT ACCOUNT=---------------#

forgotAccountManager = Blueprint('forgotManager', __name__,url_prefix=f"{prefixAccount}/forgotAccount")
forgotAccountManager.register_blueprint(forgotAccount)

#--------------------=AUTH TOKEN=--------------------#
from controllers.authManager.manageToken import tokenApp

prefixAuth="/api/authToken"
authTokenManager=Blueprint('authToken',__name__,url_prefix=f"{prefixAuth}")
authTokenManager.register_blueprint(tokenApp)
