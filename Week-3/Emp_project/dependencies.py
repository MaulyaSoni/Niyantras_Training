from fastapi import Depends , HTTPException
from fastapi.security import OAuth2PasswordBearer
from security_functions import get_current_user 
from models import Users

def emp_id_check(emp_id):
    data = emp_id
    res = data[0:3]

    return res

def verify_emp_id(current_emp_id:str=Depends(emp_id_check)):
    if res != "emp":
        raise HTTPException(status_code = 406 , detail="Not Acceptable , id should be contain the prefix of 'emp'")
    
    return res 

def verify_admin(current_user: Users = Depends(get_current_user)):
    if current_user.user_role != "Admin":
        raise HTTPException(status_code = 403 , detail="Admin access rejected")

    return current_user