import logging
from sqlalchemy.orm import Session
from fastapi import FastAPI, HTTPException , Depends , BackgroundTasks
from fastapi.security import OAuth2PasswordRequestForm
from database.db import get_db , engine
from models.model import Base , Employee , Department, Users
from schemas.user import UsersSchema , UsersResponse
from schemas.employee import EmployeeResponse , EmployeeSchema 
from schemas.department import DepartmentSchema , DepartmentResponse
from schemas.message import MessageResponse
from operations.employee import create_emp_data , update_emp , delete_emp
from operations.employee import get_all_emp , get_emp_dept_name , fetch_emp_details , fetch_emp_dept_wise 
from operations.department import create_dept , fetch_dept , delete_dept
from operations.user import create_user , create_admin
from operations.user import fetch_all_user , delete_user
from operations.token import create_token
from dependencies.admin import  verify_admin
from security.user import authenticate_user , create_access_token , get_current_user


app = FastAPI()

#---------------events-------------------------------------------------------------------

@app.on_event("startup")
def create_tables():
    # if targetted database not exist , then generates the all defined db and tables 
    Base.metadata.create_all(engine)   

#--------------create--------------------------------------------------------------------

@app.post("/employee", response_model = EmployeeResponse , status_code = 201)
def create_emp(
    emp : EmployeeSchema,
    db : Session = Depends(get_db),
    user_log : Users = Depends(get_current_user),
    current_user : dict = Depends(verify_admin)):
    return create_emp_data(db , emp , user_log)

@app.post("/department" , response_model = DepartmentResponse , status_code = 201)
def create_dept(
    dept : DepartmentSchema,
    db : Session = Depends(get_db),
    user_log : Users = Depends(get_current_user),
    current_user : dict = Depends(verify_admin)): 
    return create_dept(db , dept , user_log)

#-----------------------------------------User perspective --------------------------------------
@app.post("/register" , response_model = UsersResponse , status_code=201)
def register_user(
    user_data: UsersSchema,
    db: Session = Depends(get_db)):
    return create_user(db , user_data)

@app.post("/admin" , response_model = UsersResponse , status_code = 201)
def register_admin(
    user_data: UsersSchema,
    admin_key = str,
    db: Session = Depends(get_db)):
    return create_admin(db ,user_data , admin_key)

@app.post("/token")
def token_generation(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)):
    return create_token(db , form_data)

#-------------read------------------------------------------------------

@app.get("/department/all",response_model = list[DepartmentResponse])
def get_all_dept(
    db : Session = Depends(get_db), 
    user_log : Users = Depends(get_current_user)):
    return fetch_dept(db,user_log)

@app.get("/department/{dept_id}/employees" , response_model = list[EmployeeResponse])
def sort_emp_dept_wise(
    dept_id : str,
    db : Session = Depends(get_db),
    user_log : Users = Depends(get_current_user)):
    return fetch_emp_dept_wise(db , dept_id)

@app.get("/employee/all" , response_model = list[EmployeeResponse])
def get_all_emp_details(
    db : Session = Depends(get_db),
    user_log : Users = Depends(get_current_user)):
    return get_all_emp(db , user_log)

#------------------------------------------------------------------------------

@app.get("/employee/{emp_id}" , response_model = EmployeeResponse)
def get_emp_details(
    emp_id : str,
    db : Session = Depends(get_db),
    user_log : Users = Depends(get_current_user)):
    return fetch_emp_details(db , emp_id ,user_log)

@app.get("/employee/{emp_id}/department", response_model = DepartmentResponse)
def get_emp_dept(
    emp_id : str,
    db : Session = Depends(get_db),
    user_log : Users = Depends(get_current_user)):
    return get_emp_dept_name(db , emp_id , user_log)

#---------------------------------------------------------------

@app.get("/users/me" , response_model= UsersResponse)
def get_my_info(
    current_user: Users = Depends(get_current_user)):
    return current_user

@app.get("/users/all" , response_model = list[UsersResponse])
def get_all_users(
    db: Session = Depends(get_db),
    current_user :dict = Depends(verify_admin),
    user_log : Users = Depends(get_current_user)):
    return fetch_all_user(db ,user_log)

#-------------update--------------------------------------------------------

@app.put("/employee/update/{emp_id}" , response_model= EmployeeResponse , status_code = 200)
def update_emp_func(
    emp_id : str, 
    emp : EmployeeSchema, 
    background_tasks : BackgroundTasks, 
    db : Session = Depends(get_db),
    current_user : dict = Depends(verify_admin),
    user_log : Users = Depends(get_current_user)):
    return update_emp(db , emp_id , emp , background_tasks , user_log)

#-------------delete-----------------------------------------------------

@app.delete("/employee/delete/{emp_id}" , response_model = MessageResponse , status_code = 200)
def delete_emp_func(
    emp_id : str,
    db : Session = Depends(get_db),
    user_log : Users = Depends(get_current_user),
    current_user : dict = Depends(verify_admin)):
    return delete_emp(db , emp_id , user_log)

@app.delete("/department/delete/{dept_id}" , response_model = MessageResponse , status_code = 200)
def delete_dept_func(
    dept_id : str,
    db : Session = Depends(get_db),
    user_log : Users = Depends(get_current_user),
    current_user : dict = Depends(verify_admin)):
    return delete_dept(db , dept_id , user_log)

@app.delete("/users/delete/{userid}" , response_model = MessageResponse , status_code = 200)
def delete_user_func(
    userid : str,
    db : Session = Depends(get_db),
    user_log : Users = Depends(get_current_user),
    current_user : dict = Depends(verify_admin)):
    return delete_user(db , userid , user_log)
 

 