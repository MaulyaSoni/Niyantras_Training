from fastapi import FastAPI
from class_model import Employee
from operations import create_emp_data , fetch_details , delete_emp ,update_details , get_details_all
from fastapi.encoders import jsonable_encoder

app = FastAPI()

#CRUD

@app.post("/employee")
async def create_emp_func(emp : Employee):
    return create_emp_data(emp)

@app.get("/employee/all")
def get_all(emp:Employee):
    return get_details_all(emp)
    
@app.get("/employee/{emp_id}")
async def get_emp_func(emp_id : str):
    return fetch_details(emp_id)

@app.put("/employee/update/{emp_id}")
async def update_emp_func(emp_id : str  , emp : Employee):
    return update_details(emp_id, emp)

@app.delete("/employee/delete/{emp_id}")
async def delete_emp_func(emp_id : str):
    return delete_emp(emp_id)