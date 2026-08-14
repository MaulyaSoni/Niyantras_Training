from fastapi import FastAPI, HTTPException , Request ,Depends
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pwdlib import PasswordHash
from database import get_db , engine
from models import Base , Employee , Department
from schema import EmployeeResponse , EmployeeSchema 
from schema import DepartmentSchema , DepartmentResponse
from schema import UsersSchema , UsersResponse
from operations import create_dept_data , create_emp_data
from operations import fetch_dept , fetch_emp_details , fetch_emp_dept_wise
from operations import delete_emp , update_emp , get_all_emp , get_emp_dept_name
from operations import DataCannotInsertException , datacannotinsert_exception_handler
from operations import InvalidEmpIDException , invalid_id_exception_handler
from dependencies import verify_admin , verify_emp_id


class DataCannotInsertException(Exception):
    def __init__(self, condition):
        self.condition = condition

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

app.add_exception_handler(DataCannotInsertException , datacannotinsert_exception_handler)
app.add_exception_handler(InvalidEmpIDException , invalid_id_exception_handler)

#---------------events----------------

@app.on_event("startup")
def create_tables():
    # if not tagretted database not exist , then it generates the all defined databases
    Base.metadata.create_all(engine)   

#--------------create----------------

@app.post("/employee")
def create_emp(emp : EmployeeSchema , db : Session = Depends(get_db)):
    return create_emp_data(db , emp)

@app.post("/department")
def create_dept(dept : DepartmentSchema ,  db : Session = Depends(get_db) , current_user : dict = Depends(verify_admin)): 
    return create_dept_data(db , dept)

#-------------read-----------------------

@app.get("/employee/all")
def get_all_emp_details(emp:EmployeeResponse , db : Session = Depends(get_db)):
    return get_all_emp(db)


@app.get("/department/all")
def get_all_dept(dept:DepartmentResponse , db : Session = Depends(get_db)):
    return fetch_dept(db)


@app.get("/employee/{emp_id}")
def get_emp_details(emp_id : str , db : Session = Depends(get_db)):
    return fetch_emp_details(db , emp_id)

@app.get("/employee/{emp_id}/department")
def get_emp_dept(emp_id : str , db : Session = Depends(get_db)):
    return get_emp_dept_name(db , emp_id)

@app.get("/department/{dept_id}/Employees")
def sort_emp_dept_wise(dept_id : str , db : Session = Depends(get_db)):
    return fetch_emp_dept_wise(db , dept_id)

#-------------update----------------------

@app.put("/employee/update/{emp_id}")
def update_emp_func(emp_id : str , emp : EmployeeSchema ,db : Session = Depends(get_db)):
    return update_emp(db ,emp_id, emp)

#-------------delete-----------------------
@app.delete("/employee/delete/{emp_id}")
def delete_emp_func( emp_id : str,db : Session = Depends(get_db) , current_user : dict = Depends(verify_admin)):
    return delete_emp(db , emp_id)
