from fastapi import HTTPException , Request
from fastapi.security import OAuth2PasswordRequestForm , OAuth2PasswordBearer
from fastapi.responses import JSONResponse

#--------------------Custom Exception Classes-----------------------------

class DataCannotInsertException(Exception):
    def __init__(self, condition):
        self.condition = condition

class InvalidEmpIDException(Exception):
    pass

class DifferentIDException(Exception):
    def __init__(self , first_id , second_id):
        self.first_id = first_id
        self.second_id = second_id

async def datacannotinsert_exception_handler(request: Request, exc: DataCannotInsertException):
    return JSONResponse(
        status_code=409,
        content={"message": f"You can't insert a duplicate data , {exc.condition}"},
    )

async def invalid_id_exception_handler(request :Request , exc : InvalidEmpIDException):
    return JSONResponse(
        status_code = 400,
        content = {"message" : f"You breaking syntax for company's employee ID "}
    )

async def different_id_exception_handler(request : Request , exc : DifferentIDException):
    return JSONResponse(
        status_code = 409,
        content = {"message" : f"You can't altered the employee ID"}
    ) 


#------------------------logger----------------------------

def update_notification(emp_id:str):
    return(f"{emp_id}Employee was updated")

#-----------------------------------------------------------