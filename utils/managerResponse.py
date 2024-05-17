from utils import codes as iCodes


def Errors(error,errorCode:iCodes=None):
    #vars funciona parecido a dict
    return vars(rErrors(error,errorCode))

def Success(success):
    return vars(rSuccess(success))

class rErrors:
    def __init__(self,error,errorCode:iCodes=None):
        self.error=error
        if(errorCode!=None):self.errorCode=errorCode
        
class rSuccess:
    def __init__(self,success:str):
         self.success=success