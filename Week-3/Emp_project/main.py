from fastapi import FastAPI
from class_model import Employee
from operations import create_emp_data , fetch_details

app = FastAPI()

#CRUD
@app.post("/employee/")
async def create_emp_data(emp : Employee):
    return create_emp_data(emp)

@app.get("/employee/{emp_id}")
async def fetch_details(emp :Employee , emp_id : str):
    return fetch_details(emp_id)

@app.put("/employee/update/{emp_id}")
async def update_details(emp_id :str , updated_name : str  , updated_age : int):
    updated_item = jsonable_emcoder(Employee)
    Employee[emp_id] = updated_item
    return updated_item  