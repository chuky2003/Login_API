from flask import Blueprint

# Crear una instancia de Blueprint



#---------------------------------------------
#---------------LOGIN REGISTER----------------
#---------------------------------------------
from controllers.accountManager.registerAccount import registerApp
from controllers.accountManager.loginAccount import loginAPP
from controllers.authManager.logOut import logOutApp
from controllers.accountManager.forgotAccount import forgotAccount


prefixAccount = "/api/accountManager"
accountManager = Blueprint('accountManager', __name__,url_prefix=prefixAccount)

accountManager.register_blueprint(loginAPP)
accountManager.register_blueprint(registerApp)

#---------------------=FORGOT ACCOUNT=---------------#

forgotAccountManager = Blueprint('forgotManager', __name__,url_prefix=f"{prefixAccount}/forgotAccount")
forgotAccountManager.register_blueprint(forgotAccount)