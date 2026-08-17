from fastapi import FastAPI, HTTPException , Request ,Depends , BackgroundTasks
from typing import Annotated
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm , OAuth2PasswordBearer
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from pwdlib import PasswordHash
from database import get_db , engine
from models import Base , Employee , Department, Users
from schema import EmployeeResponse , EmployeeSchema 
from schema import DepartmentSchema , DepartmentResponse
from schema import UsersSchema , UsersResponse
from operations import create_dept_data , create_emp_data , create_user
from operations import fetch_dept , fetch_emp_details , fetch_emp_dept_wise , fetch_all_user
from operations import delete_emp , update_emp , get_all_emp , get_emp_dept_name
from operations import DataCannotInsertException , datacannotinsert_exception_handler
from operations import InvalidEmpIDException , invalid_id_exception_handler , update_notification
from dependencies import get_current_user, verify_admin , verify_emp_id
from security_functions import authenticate_user , create_access_token
# from operations import create_admin

class DataCannotInsertException(Exception):
    def __init__(self, condition):
        self.condition = condition

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

app = FastAPI()

app.add_exception_handler(DataCannotInsertException , datacannotinsert_exception_handler)
app.add_exception_handler(InvalidEmpIDException , invalid_id_exception_handler)

#---------------events-------------------------------------------------------------------

@app.on_event("startup")
def create_tables():
    # if not tagretted database not exist , then it generates the all defined databases
    Base.metadata.create_all(engine)   

#--------------create--------------------------------------------------------------------

@app.post("/employee")
def create_emp(emp : EmployeeSchema , db : Session = Depends(get_db) , current_user : dict = Depends(verify_admin)):
    return create_emp_data(db , emp)

@app.post("/department")
def create_dept(dept : DepartmentSchema ,  db : Session = Depends(get_db) , current_user : dict = Depends(verify_admin)): 
    return create_dept_data(db , dept)

#-----------------------------------------User perspective --------------------------------------
@app.post("/register")
def register(user_data: UsersSchema,db: Session = Depends(get_db)):
    return create_user(db,user_data)

# @app.post("/admin")
# def register(user_data: UsersSchema,db: Session = Depends(get_db)):
#     return create_admin(db,user_data)

@app.post("/token")
def login(form_data: OAuth2PasswordRequestForm = Depends(),db: Session = Depends(get_db)):
    user = authenticate_user(db,form_data.username,form_data.password)
    if user is None:
        raise HTTPException(status_code=401,detail="Incorrect username or password")
    token = create_access_token(user.username)
    return {"access_token": token,"token_type": "bearer"}

#-------------read------------------------------------------------------

@app.get("/department/all")
def get_all_dept(dept:DepartmentResponse , db : Session = Depends(get_db)):
    return fetch_dept(db)

@app.get("/department/{dept_id}/Employees")
def sort_emp_dept_wise(dept_id : str , db : Session = Depends(get_db)):
    return fetch_emp_dept_wise(db , dept_id)

#------------------------------------------------------------------------------
@app.get("/employee/all")
def get_all_emp_details(emp:EmployeeResponse , db : Session = Depends(get_db)):
    return get_all_emp(db)

@app.get("/employee/{emp_id}")
def get_emp_details(emp_id : str , db : Session = Depends(get_db)):
    return fetch_emp_details(db , emp_id)


@app.get("/employee/{emp_id}/department")
def get_emp_dept(emp_id : str , db : Session = Depends(get_db)):
    return get_emp_dept_name(db , emp_id)


#---------------------------------------------------------------
@app.get("/users/me")
def get_my_profile(current_user: Users = Depends(get_current_user)):
    return current_user()

@app.get("/users/all")
def get_all_users(users = UsersResponse , db: Session = Depends(get_db) , current_user :dict = Depends(verify_admin)):
    return fetch_all_user(db)

#-------------update--------------------------------------------------------
@app.put("/employee/update/{emp_id}")
def update_emp_func(
    emp_id : str, 
    emp : EmployeeSchema, 
    background_tasks : BackgroundTasks, 
    db : Session = Depends(get_db),
    current_user : dict = Depends(verify_admin)):
    return update_emp(db ,emp_id, emp , background_tasks)

#-------------delete-----------------------------------------------------
@app.delete("/employee/delete/{emp_id}")
def delete_emp_func(
    emp_id : str,
    db : Session = Depends(get_db),
    current_user : dict = Depends(verify_admin)):
    return delete_emp(db , emp_id)