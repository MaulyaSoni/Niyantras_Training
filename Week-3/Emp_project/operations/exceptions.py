import logging
from fastapi import HTTPException , Depends , Request
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm , OAuth2PasswordBearer
from fastapi.responses import JSONResponse

logging.basicConfig(
    filename="Log_employee_project.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

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
