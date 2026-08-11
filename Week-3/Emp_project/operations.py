from fastapi import HTTPException 
from sqlalchemy.orm import Session
from models import Employee ,Department
from schema import EmployeeSchema , EmployeeResponse , DepartmentSchema , DepartmentResponse


def create_dept_data(db : Session , dept : DepartmentSchema):

    department_check = db.get(Department , dept.dept_id)
    
    if department_check:
        raise HTTPException(status_code = 400 , detail = "!!Department already created ")
    
    department = Department(dept_id = dept.dept_id , dept_name = dept.dept_name)
    db.add(department)
    db.commit()

    return {"Department details inserted successfully..."}

def create_emp_data(db : Session , emp : EmployeeSchema):

    existing_emp = db.get(Employee ,emp.e_id)
    department = db.get(Department ,emp.dept_id)

    if department is None :
        raise HTTPException(status_code=404,detail = "Department not exists...")
    
    if existing_emp :
        raise HTTPException(status_code = 400 ,detail = "!! Employee already exist...")  
    
    employee = Employee(e_id = emp.e_id , name = emp.name  , age = emp.age , dept_id = emp.dept_id)
    db.add(employee)
    db.commit()

    return{"New employee added successfully "}



def get_all_emp(db:Session):

    return db.query(Employee).all()

def fetch_dept(db : Session):

    return db.query(Department).all()

def fetch_emp_details(db : Session , emp_id : str):

    employee = db.get(Employee , emp_id)
    if employee is None :
        raise HTTPException(status_code = 404 , detail = "Employee Not Found...")
    
    return employee

def fetch_emp_dept_wise(db : Session , dept_id : str):

    department = db.get(Department , dept_id)

    if department is None :
        raise HTTPException(status_code = 404 , detail = "..Departent does'nt exist..")

    return department.employee_object
    


def update_emp(db : Session , emp_id : str , emp : EmployeeSchema):

    employee =  db.get(Employee , emp_id)
    
    if employee is None :
        raise HTTPException(status_code = 404 , detail = "User not found for updating the data")
    
    employee.name =  emp.name
    employee.age = emp.age
    db.commit()
    db.refresh(employee)

    return {"Employee details update successfully "}

def delete_emp(db : Session , emp_id : str ):

    employee = db.get(Employee , emp_id)
    if employee is None:
        raise HTTPException(status_code = 404 , detail = "!! Unable to delete !!..Employee data not found..")

    db.delete(employee)
    db.commit()

    return {f"Employee {emp_id} deleted successfully"}