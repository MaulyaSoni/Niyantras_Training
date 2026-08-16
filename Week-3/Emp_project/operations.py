import logging
from typing import Annotated
from fastapi import HTTPException , Depends ,Request
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session
from models import Employee ,Department
from schema import EmployeeSchema , EmployeeResponse , DepartmentSchema , DepartmentResponse , UsersSchema , UsersResponse
from models import Users 
from hash_methods import generate_hash_password
logging.basicConfig(
    filename="Emp_project.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Custom class 1
class DataCannotInsertException(Exception):
    def __init__(self, condition):
        self.condition = condition

async def datacannotinsert_exception_handler(request: Request, exc: DataCannotInsertException):
    return JSONResponse(
        status_code=409,
        content={"message": f"You can't insert a duplicate data"},
    )

# Custom class 2
class InvalidEmpIDException(Exception):
    pass

async def invalid_id_exception_handler(request :Request , exc : InvalidEmpIDException):
    return JSONResponse(
        status_code = 400,
        content = {"message" : f"You can't have this prefix in employee ID , try this 'emp'"}
    )

# Custom class 3 
class DifferentIDException(Exception):
    def __init__(self , first_id , second_id):
        self.first_id = first_id
        self.second_id = second_id

async def different_id_exception_handler(request : Request , exc : DifferentIDException):
    return JSONResponse(
        status_code = 409,
        content = {"message" : f"You can't altered the employee ID"}
    ) 

# methods 
def create_emp_data(db : Session , emp : EmployeeSchema):

    existing_emp = db.get(Employee ,emp.e_id)
    department = db.get(Department ,emp.dept_id)

    if department is None :
        raise HTTPException(status_code=404,detail = "Department not exists...")
    
    try:
        if existing_emp:
            logging.warning(f"Duplicate Employee data insertion error")
            raise DataCannotInsertException(condition = existing_emp)
            # raise HTTPException(status_code = 400 , detail = "!!Department already created ")
    except DataCannotInsertException as e:
        raise HTTPException(status_code=409,detail="Duplicate Data can't be inserted ")    
    
    data = emp.e_id
    res = data[0:3]
    try:
        if res != "emp":
            logging.warning(f"ID not match with prefix error")
            raise InvalidEmpIDException()
    except InvalidEmpIDException as e: 
        raise HTTPException(status_code = 401 , detail = "Invalid ID syntax")

    employee = Employee(e_id = emp.e_id , name = emp.name  , age = emp.age , dept_id = emp.dept_id)
    db.add(employee)
    db.commit()

    return{"New employee added successfully "}


def create_dept_data(db : Session , dept : DepartmentSchema):

    department_check = db.get(Department , dept.dept_id)
    
    try:
        if department_check:
            logging.error("Department not found error")
            raise DataCannotInsertException(condition = department_check)
            # raise HTTPException(status_code = 400 , detail = "!!Department already created ")
    
    except DataCannotInsertException as e:
        raise HTTPException(status_code=409,detail="Duplicate Data can't be inserted ")    
    
    department = Department(dept_id = dept.dept_id , dept_name = dept.dept_name)
    db.add(department)
    db.commit()

    return {"Department details inserted successfully..."}

def create_user(db: Session,user_data: UserCreate):

    existing_user = (db.query(Users).filter(Users.username == user_data.username).first())

    if existing_user:
        raise HTTPException(status_code=409,detail="Username already exists")

    new_user = User(userid="user001",username=user_data.username,
        generate_hashed_password=hash_password(user_data.password),user_role="user")

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user

def get_all_emp(db:Session):
    # logging.info("Fetching all employee details")
    return db.query(Employee).all()

def fetch_dept(db : Session):
    # logging.info("Fetching all department details")
    return db.query(Department).all()

def fetch_emp_details(db : Session , emp_id : str):

    employee = db.get(Employee , emp_id)
    if employee is None :
        logging.error(f"{emp_id} : not found error in get emp")
        raise HTTPException(status_code = 404 , detail = "Employee Not Found...")
    
    return employee

def fetch_emp_dept_wise(db : Session , dept_id : str):

    department = db.get(Department , dept_id)

    if department is None :
        logging.error(f"{dept_id} not found error in sort (get) emp/dept")
        raise HTTPException(status_code = 404 , detail = "..Departent does'nt exist..")

    return department.employee_object
    
def get_emp_dept_name(db:Session , emp_id : str):
    employee = db.get(Employee , emp_id)
    if employee is None:
        logging.error(f"{emp_id} not found error in get emp/dept_name ")
        raise HTTPException(status_code = 404 , detail = " Invalid Input , Employee not found " )
    
    dept_id = employee.dept_id
    department = db.get(Department , dept_id)
    return department


def update_emp(db : Session , emp_id : str , emp : EmployeeSchema):

    employee =  db.get(Employee , emp_id)
    
    if employee is None :
        logging.info(f"{user_id} , updation error ")
        raise HTTPException(status_code = 404 , detail = "User not found for updating the data")
    
    try:
        if employee.e_id != emp.e_id:
            logging.warning("ID altering in update_emp function")
            raise DifferentIDException(employee.e_id,emp.e_id)

    except DifferentIDException as e:
        raise HTTPException(status_code = 409 , detail =" Employee ID can't change during details updatetion")

    employee.name = emp.name
    employee.age = emp.age
    db.commit()
    db.refresh(employee)

    return {"Employee details update successfully "}


def delete_emp(db : Session , emp_id : str ):

    employee = db.get(Employee , emp_id)
    if employee is None:
        logging.error("employee not found in delete function ")
        raise HTTPException(status_code = 404 , detail = "!! Unable to delete !!..Employee data not found..")

    db.delete(employee)
    db.commit()

    return {f"Employee {emp_id} deleted successfully"}



