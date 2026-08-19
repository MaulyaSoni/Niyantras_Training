import logging
from fastapi import HTTPException , Depends ,  Request , BackgroundTasks
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer
from fastapi.responses import JSONResponse
from models import Employee , Department , Users
from schema import EmployeeSchema , EmployeeResponse 
from schema import DepartmentSchema , DepartmentResponse 
from schema import UsersSchema , UsersResponse
from hash_methods import generate_hash_password
from security_functions import get_current_user
import os
#ADMIN_KEY = os.getenv("ADMIN_KEY")

logging.basicConfig(
    filename="Log_employee_project.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)
#--------------------Custom Exception Classes-----------------------------

class DataCannotInsertException(Exception):
    def __init__(self, condition):
        self.condition = condition

class InvalidEmpIDException(Exception):
    pass

class DifferentIDException(Exception):
    def __init__(self , first_id , second_id):
        self.first_id = first_id
        self.second_id = second_id

async def datacannotinsert_exception_handler(request: Request, exc: DataCannotInsertException):
    return JSONResponse(
        status_code=409,
        content={"message": f"You can't insert a duplicate data , {exc.condition}"},
    )

async def invalid_id_exception_handler(request :Request , exc : InvalidEmpIDException):
    return JSONResponse(
        status_code = 400,
        content = {"message" : f"You breaking syntax for company's employee ID "}
    )

async def different_id_exception_handler(request : Request , exc : DifferentIDException):
    return JSONResponse(
        status_code = 409,
        content = {"message" : f"You can't altered the employee ID"}
    ) 

#---------------------logger----------------------------------

def update_notification(emp_id:str):
    return(f"{emp_id}Employee was updated")

#---------------------------Create----------------------------------
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
    
    try:
        if (res := emp.e_id[0:3]) != "emp":
            logging.warning(f"ID not match with prefix ")
            raise InvalidEmpIDException()

    except InvalidEmpIDException as e: 
        raise HTTPException(status_code = 401 , detail = "Invalid ID syntax , make sure it matches with company's id")

    employee = Employee(e_id = emp.e_id , name = emp.name  , age = emp.age , dept_id = emp.dept_id)
    db.add(employee)
    db.commit()
    logging.info(f"{emp.e_id} , New employee created")
    return employee

def create_dept_data(db : Session , dept : DepartmentSchema):
    department_check = db.get(Department , dept.dept_id)
    
    try:
        if department_check:
            logging.warning("Duplicate Department Data insertion")
            raise DataCannotInsertException(condition = department_check)
            # raise HTTPException(status_code = 400 , detail = "!!Department already created ")
    
    except DataCannotInsertException as e:
        raise HTTPException(status_code=409,detail="Duplicate Department Data can't be inserted ")    
    
    department = Department(dept_id = dept.dept_id , dept_name = dept.dept_name)
    db.add(department)
    db.commit()
    logging.info(f"{dept.dept_id} , New Department created")
    return department

def create_user(db: Session,user_data: UsersSchema):
    existing_user = (db.query(Users).filter(Users.username == user_data.username).first())

    if existing_user:
        logging.warning("Duplicate User details input ")
        raise HTTPException(status_code=409,detail="User already exists")

    # new_user = Users(userid="user001",username=user_data.username,
    #     hashed_password=generate_hash_password(user_data.password),user_role="user")

    new_user = Users(username=user_data.username,
        hashed_password=generate_hash_password(user_data.password),user_role="user")

    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    logging.info("New User created")
    return new_user

def create_admin(db:Session , user_data : UsersSchema):

    # if user_data.admin_key != ADMIN_KEY :
    #    return {"message":"admin key not matched"}

    new_user = Users(username=user_data.username,
    hashed_password=generate_hash_password(user_data.password),user_role="Admin")

    db.add(new_user)
    db.commit()
    return new_user
   

#-----------------------------read-----------------------------

def get_all_emp(db:Session):
    logging.info("Fetching all employee details")
    return db.query(Employee).all()

def fetch_dept(db : Session):
    logging.info("Fetching all department details")
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

def fetch_all_user(db:Session):
    return db.query(Users).all()

#----------------Update----------------------

def update_emp(db : Session , emp_id : str , emp : EmployeeSchema , background_tasks : BackgroundTasks):
    employee =  db.get(Employee , emp_id)
    
    if employee is None :
        logging.warning(f"{emp_id} , employee not found while updating ")
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
    # current_user = get_current_user()
    background_tasks.add_task(update_notification , emp_id)
    logging.info(f"{emp_id} , employee updated ")
    
    return employee

#-----------------------Delete-----------------------------------------------------------

def delete_emp(db : Session , emp_id : str ):

    employee = db.get(Employee , emp_id)
    if employee is None:
        logging.warning("employee not found in delete function ")
        raise HTTPException(status_code = 404 , detail = "!! Unable to delete !!..Employee data not found..")

    db.delete(employee)
    db.commit()
    logging.info(f"{emp_id} , employee deleted ")
    return f"Employee {emp_id} deleted successfully"

def delete_dept(db:Session , dept_id : str ):

    department = db.get(Department , dept_id)

    if department is None :
        logging.error(f"{dept_id} not found error in sort (get) emp/dept")
        raise HTTPException(status_code = 404 , detail = "..Departent does'nt exist..")
   
    if department.employee_object:
        logging.error(f"trying to delete Department containing emp")
        raise HTTPException(status_code = 403 , detail = "can't delete , the department contains employee ")
    
    db.delete(department)
    db.commit()
    return f"{dept_id} , department deleted successfully"


def delete_user(db: Session , userid : str):
    
    user = db.get(Users , userid)
    if user is None:
        raise HTTPException(status_code = 404 , detail="user not found")
    
    db.delete(user)
    db.commit()
    return f"{userid} , deleted successfully"

#----------------------------------------------------------------------------------------