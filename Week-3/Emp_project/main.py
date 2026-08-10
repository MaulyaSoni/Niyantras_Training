from fastapi import FastAPI , Depends
from sqlalchemy.orm import Session
from class_model import EmployeeModel
from database import engine
from models import Employee , Base
from schema import EmployeeResponse , EmployeeSchema
from operations import create_emp_data , fetch_details , delete_emp ,update_details , get_details_all
from database import get_db

app = FastAPI()

#CRUD

# @app.post("/employee")
# async def create_emp_func(emp : EmployeeModel):
#     return create_emp_data(emp)

# @app.get("/employee/all")
# def get_all(emp:EmployeeModel):
#     return get_details_all(emp)
    
# @app.get("/employee/{emp_id}")
# async def get_emp_func(emp_id : str):
#     return fetch_details(emp_id)

# @app.put("/employee/update/{emp_id}")
# async def update_emp_func(emp_id : str  , emp : EmployeeModel):
#     return update_details(emp_id, emp)

# @app.delete("/employee/delete/{emp_id}")
# async def delete_emp_func(emp_id : str):
#     return delete_emp(emp_id)

@app.on_event("startup")
def create_tables():
    # if not tagretted database not exist , then it generates the all defined databases
    Base.metadata.create_all(engine)    

@app.post("/employee")
async def create_emp_func(emp : EmployeeSchema , db : Session = Depends(get_db)):
    return create_emp_data(db ,emp)

@app.get("/employee/all")
def get_all(emp:EmployeeResponse , db : Session = Depends(get_db)):
    return get_details_all(db)
    
@app.get("/employee/{emp_id}")
async def get_emp_func(emp_id : str , db : Session = Depends(get_db)):
    return fetch_details(db , emp_id)

@app.put("/employee/update/{emp_id}")
async def update_emp_func(emp_id : str , emp : EmployeeSchema ,db : Session = Depends(get_db)):
    return update_details(db ,emp_id, emp)

@app.delete("/employee/delete/{emp_id}")
async def delete_emp_func( emp_id : str,db : Session = Depends(get_db) ):
    return delete_emp(db , emp_id)