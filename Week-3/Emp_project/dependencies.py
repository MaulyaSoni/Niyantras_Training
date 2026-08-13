from fastapi import Depends , HTTPException

def get_current_user():
    return{
        "username" : "MS",
        "role":"Admin"
    }

def verify_admin(current_user : dict = Depends(get_current_user)):
    if current_user["role"] != "Admin":
        raise HTTPException(status_code = 400 , detail="..You don't have access (Admin access rejected)..")
    
    return current_user


def emp_id_check(emp_id):
    data = emp_id
    res = data[0:3]
    return res

def verify_emp_id(current_emp_id:str=Depends(emp_id_check)):
    if res != "emp":
        raise HTTPException(status_code = 406 , detail="Not Acceptable , id should be contain the prefix of 'emp'")
    
    return res 

