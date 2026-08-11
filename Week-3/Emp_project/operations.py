from fastapi import HTTPException 
from models import Employee
from class_model import EmployeeModel
from schema import EmployeeSchema , EmployeeResponse
from sqlalchemy.orm import Session
# emp_list = []

def get_details_all(db:Session):
    # if emp_list:
    #     return {f"Employee Data : {emp_list}"}
    # raise HTTPException(status_code = 404 , detail = "Employee list data not found")

    return db.query(Employee).all()

def fetch_details(db : Session , emp_id : str):

    employee = db.get(Employee , emp_id)

    if employee is None :
        raise HTTPException(status_code = 400 , detail = "Employee Not Found...")
    
    return employee

    # for e in emp_list:
    #     if e.e_id == emp_id:
    #         return {f"Employee found : {e}"}


def create_emp_data(db : Session , emp : EmployeeSchema):
    
    existing_emp = db.get(Employee ,emp.e_id)
    
    if existing_emp :
        raise HTTPException(status_code = 400 ,detail = "!! Employee already exist...")
    
    # for e in emp_list:
    #     if e.e_id == emp.e_id:
    #         raise HTTPException(status_code = 400 ,detail = "Same name employee already exist...")
    # emp_list.append(emp)
    # return{f"Employee Created Successfully...{emp.e_id}"}

    employee = Employee(e_id = emp.e_id , name = emp.name  , age = emp.age)
    db.add(employee)
    db.commit()
    return{"New employee added successfully "}

def update_details(db : Session , emp_id : str , emp : EmployeeSchema):
    employee =  db.get(Employee , emp_id)
    
    if employee is None :
        raise HTTPException(status_code = 404 , detail = "User not found for updating the data")
    
    employee.name =  emp.name
    employee.age = emp.age
    db.commit()
    db.refresh(employee)

    return {"Employee details update successfully "}

    # for index , e in emp_list:
    #     if e.e_id == emp_id:
    #         emp_list[emp_id] = emp
    #         return {"Change successfully.."}


def delete_emp(db : Session , emp_id : str ):

    employee = db.get(Employee , emp_id)
    if employee is None:
        raise HTTPException(status_code = 404 , detail = "!! Unable to delete !!..Employee data not found..")

    # for e in emp_list:
    #     if e.e_id == emp_id:
    #         emp_list.remove(e)

    db.delete(employee)
    db.commit()
    
    return {f"Employee {emp_id} deleted successfully"}
