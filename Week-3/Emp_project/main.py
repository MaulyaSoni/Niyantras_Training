from fastapi import FastAPI , Depends
from typing import Annotated
from sqlalchemy.orm import Session
from database import get_db , engine
from models import Base , Employee , Department
from schema import EmployeeResponse , EmployeeSchema , DepartmentSchema , DepartmentResponse
from operations import create_dept_data , create_emp_data
from operations import fetch_dept , fetch_emp_details , fetch_emp_dept_wise
from operations import delete_emp , update_emp , get_all_emp
from dependencies import verify_admin , verify_emp_id
from fastapi.security import OAuth2PasswordBearer

app = FastAPI()

@app.on_event("startup")
def create_tables():
    # if not tagretted database not exist , then it generates the all defined databases
    Base.metadata.create_all(engine)    


@app.post("/employee")
def create_emp(emp : EmployeeSchema , db : Session = Depends(get_db)):
    return create_emp_data(db ,emp)

@app.post("/department")
def create_dept(dept : DepartmentSchema ,  db : Session = Depends(get_db) , current_user : dict = Depends(verify_admin)): 
    return create_dept_data(db , dept)


# @app.get("/admin")
# def verify_admin_func()

@app.get("/employee/all")
def get_all_emp_details(emp:EmployeeResponse , db : Session = Depends(get_db)):
    return get_all_emp(db)


@app.get("/department/all")
def get_all_dept(dept:DepartmentResponse , db : Session = Depends(get_db)):
    return fetch_dept(db)


@app.get("/employee/{emp_id}")
def get_emp_details(emp_id : str , db : Session = Depends(get_db)):
    return fetch_emp_details(db , emp_id)


@app.get("/department/{dept_id}/Employees")
def get_emp_dept_wise(dept_id : str , db : Session = Depends(get_db)):
    return fetch_emp_dept_wise(db , dept_id)



@app.put("/employee/update/{emp_id}")
def update_emp_func(emp_id : str , emp : EmployeeSchema ,db : Session = Depends(get_db)):
    return update_emp(db ,emp_id, emp)


@app.delete("/employee/delete/{emp_id}")
def delete_emp_func( emp_id : str,db : Session = Depends(get_db) , current_user : dict = Depends(verify_admin)):
    return delete_emp(db , emp_id)

# @app.delete("/employee/delete/all")
# def delete_all_func(db : Session = Depends(get_db) , current_user : dict = Depends(verify_admin)):
#     return delete_all(db)
