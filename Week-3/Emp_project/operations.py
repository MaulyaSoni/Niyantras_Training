from fastapi import HTTPException
from class_model import Employee

emp_list = []

def get_details_all(emp):
    if emp_list:
        return {f"Employee Data : {emp_list}"}
    raise HTTPException(status_code = 404 , detail = "Employee list data not found")

def fetch_details(emp_id):
    for e in emp_list:
        if e.e_id == emp_id:
            return {f"Employee found : {e}"}

    raise HTTPException(status_code = 400 , detail = "Employee Not Found...")

def create_emp_data(emp):
    for e in emp_list:
        if e.e_id == emp.e_id:
            raise HTTPException(status_code = 400 ,detail = "Same name employee already exist...")
    emp_list.append(emp)
    return{"Employee Created Successfully.."}

def delete_emp(emp_id):
    for e in emp_list:
        if e.e_id == emp_id:
            emp_list.remove(e)
            return {f"Employee {emp_id} deleted successfully"}
    raise HTTPException(status_code = 404 , detail = "!! Unable to delete !!..Employee data not found..")

async def update_details(emp_id ,emp):
    # temp = await request.json()
    # updated_name = temp["name"]
    # updated_age = temp["age"]

    for e in emp_list:
        if e.e_id == emp_id:
            # e["name"] = updated_name
            # e["age"] = updated_age
            emp_list[emp_id] = emp.model_dump()
            return {"Change successfully.."}

    raise HTTPException(status_code = 404 , detail = "User not found for updating the data")