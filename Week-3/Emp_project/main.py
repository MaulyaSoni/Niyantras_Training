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
from operations.department import create_dept_data , fetch_dept , delete_dept
from operations.user import create_user , create_admin
from operations.user import fetch_all_user , delete_user
from operations.token import create_token
from dependencies.admin import  verify_admin
from dependencies.context import get_admin_context
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
    context = Depends(get_admin_context)):
    
    return create_emp_data(context["db"] , emp  , context["current_user"])

@app.post("/department" , response_model = DepartmentResponse , status_code = 201)
def create_dept(
    dept : DepartmentSchema,
    context = Depends(get_admin_context)

    ): 

    return create_dept_data(context["db"]  ,dept )

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
    context = Depends(get_admin_context)):
   
    return fetch_dept(context["db"] , context["current_user"])

@app.get("/employee/all" , response_model = list[EmployeeResponse])
def get_all_emp_details(
    context = Depends(get_admin_context)):

    return get_all_emp(context["db"] , context["current_user"])

@app.get("/users/all" , response_model = list[UsersResponse])
def get_all_users(
    context = Depends(get_admin_context)):
   
    return fetch_all_user(context["db"],context["current_user"])

#------------------------------------------------------------------------------

@app.get("/department/{dept_id}/employees" , response_model = list[EmployeeResponse])
def sort_emp_dept_wise(
    dept_id : str,
    db : Session = Depends(get_db),
    user_log : Users = Depends(get_current_user)):
    return fetch_emp_dept_wise(db , dept_id)

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


#-------------update--------------------------------------------------------

@app.put("/employee/update/{emp_id}" , response_model= EmployeeResponse , status_code = 200)
def update_emp_func(
    emp_id : str, 
    emp : EmployeeSchema, 
    background_tasks : BackgroundTasks,
    context = Depends(get_admin_context)):
   
    return update_emp(context["db"] , emp_id , emp , background_tasks , context["current_user"])

#-------------delete-----------------------------------------------------

@app.delete("/employee/delete/{emp_id}" , response_model = MessageResponse , status_code = 200)
def delete_emp_func(
    emp_id : str,
    context = Depends(get_admin_context)):
    return delete_emp(context["db"] , emp_id , context["current_user"])

@app.delete("/department/delete/{dept_id}" , response_model = MessageResponse , status_code = 200)
def delete_dept_func(
    dept_id : str,
    context = Depends(get_admin_context)):
    return delete_dept(context["db"] , dept_id , context["current_user"])

@app.delete("/users/delete/{userid}" , response_model = MessageResponse , status_code = 200)
def delete_user_func(
    userid : str,
    context = Depends(get_admin_context)):
    
    return delete_user(context["db"] , userid , context["current_user"])
 

 