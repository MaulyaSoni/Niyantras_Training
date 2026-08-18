from fastapi import FastAPI, HTTPException , Request ,Depends , BackgroundTasks
import logging
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm
from fastapi.exceptions import RequestValidationError
from fastapi.responses import JSONResponse
from database import get_db , engine
from models import Base , Employee , Department, Users
from schema import EmployeeResponse , EmployeeSchema 
from schema import DepartmentSchema , DepartmentResponse
from schema import UsersSchema , UsersResponse
from operations import create_dept_data , create_emp_data , create_user
from operations import fetch_dept , fetch_emp_details , fetch_emp_dept_wise , fetch_all_user
from operations import update_emp , get_all_emp , get_emp_dept_name
from operations import delete_emp , delete_dept
from operations import DataCannotInsertException , datacannotinsert_exception_handler
from operations import InvalidEmpIDException , invalid_id_exception_handler 
from operations import DifferentIDException , different_id_exception_handler , update_notification
from dependencies import get_current_user, verify_admin , verify_emp_id
from security_functions import authenticate_user , create_access_token
# from operations import create_admin

app = FastAPI()

#---------------events-------------------------------------------------------------------

@app.on_event("startup")
def create_tables():
    # if targetted database not exist , then generates the all defined db and tables 
    Base.metadata.create_all(engine)   

#--------------create--------------------------------------------------------------------

@app.post("/employee")
def create_emp(
    emp : EmployeeSchema,
    db : Session = Depends(get_db),
    current_user : dict = Depends(verify_admin)):
    return create_emp_data(db , emp)

@app.post("/department")
def create_dept(
    dept : DepartmentSchema,
    db : Session = Depends(get_db),
    current_user : dict = Depends(verify_admin)): 
    return create_dept_data(db , dept)

#-----------------------------------------User perspective --------------------------------------
@app.post("/register")
def register(user_data: UsersSchema,db: Session = Depends(get_db)):
    return create_user(db,user_data)

# @app.post("/admin")
# def register(user_data: UsersSchema,db: Session = Depends(get_db)):
#     return create_admin(db,user_data)

@app.post("/token")
def token_generation(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db)):
    
    user = authenticate_user(db,form_data.username,form_data.password)
    
    if user is None:
        raise HTTPException(status_code=401,detail="Incorrect username or password")
    token = create_access_token(user.username)
    logging.info(f"Access token created for {user}")
    return {"access_token": token,"token_type": "bearer"}

#-------------read------------------------------------------------------

@app.get("/department/all")
def get_all_dept(dept:DepartmentResponse , db : Session = Depends(get_db)):
    return fetch_dept(db)

@app.get("/department/{dept_id}/employees")
def sort_emp_dept_wise(dept_id : str , db : Session = Depends(get_db)):
    return fetch_emp_dept_wise(db , dept_id)

#------------------------------------------------------------------------------
@app.get("/employee/all")
def get_all_emp_details(
    emp: EmployeeResponse,
    db : Session = Depends(get_db)):
    return get_all_emp(db)

@app.get("/employee/{emp_id}")
def get_emp_details(
    emp_id : str,
    db : Session = Depends(get_db)):
    return fetch_emp_details(db , emp_id)

@app.get("/employee/{emp_id}/department")
def get_emp_dept(
    emp_id : str,
    db : Session = Depends(get_db)):
    return get_emp_dept_name(db , emp_id)

#---------------------------------------------------------------
@app.get("/users/me")
def get_my_info(current_user: Users = Depends(get_current_user)):
    return{"userid":current_user.userid , "username" : current_user.username}

@app.get("/users/all")
def get_all_users(
    users = UsersResponse,
    db: Session = Depends(get_db),
    current_user :dict = Depends(verify_admin)):
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

@app.delete("/department/delete/{dept_id}")
def delete_dept_func(
    dept_id : str,
    db : Session = Depends(get_db),
    current_user : dict = Depends(verify_admin)):
    return delete_dept(db , dept_id )