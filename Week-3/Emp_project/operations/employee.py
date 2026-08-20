import os
import logging
from sqlalchemy.orm import Session
from fastapi import HTTPException , Depends ,  BackgroundTasks
from models.model import Employee , Department , Users
from schemas.employee import EmployeeSchema , EmployeeResponse 
from schemas.department import DepartmentSchema , DepartmentResponse 
from operations.exceptions import DataCannotInsertException , datacannotinsert_exception_handler
from operations.exceptions import InvalidEmpIDException , invalid_id_exception_handler 
from operations.exceptions import DifferentIDException , different_id_exception_handler
from operations.exceptions import update_notification

import structlog

logger = structlog.get_logger()

logging.basicConfig(
    filename="Log_employee_project.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

#--------------------------------------------------------------------------

def create_emp_data(
    db : Session,
    emp : EmployeeSchema,
    user_log : Users):

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
        if(res := emp.e_id[0:3]) != "emp":
            logging.warning(f"ID not match with prefix ")
            raise InvalidEmpIDException()

    except InvalidEmpIDException as e: 
        raise HTTPException(status_code = 401 , detail = "Invalid ID syntax , make sure it matches with company's id")

    employee = Employee(
        e_id = emp.e_id,
        name = emp.name,
        age = emp.age,
        dept_id = emp.dept_id
    )
    db.add(employee)
    db.commit()
    logging.info(f"{emp.e_id} , New employee created by '{user_log.username}'")
    return employee

#----------------------------------------------------------

def get_all_emp(
    db:Session,
    user_log : Users):

    logging.info(f"Fetch all emp details by '{user_log.username}'")
    return db.query(Employee).all()

def fetch_emp_details(
    db : Session,
    emp_id : str,
    user_log : Users):

    employee = db.get(Employee , emp_id)
    if employee is None :
        logging.error(f"{emp_id} : not found error in get emp")
        raise HTTPException(status_code = 404 , detail = "Employee Not Found...")
    logging.info(f"Fetch emp {emp_id} details by '{user_log.username}'")
    return employee

def fetch_emp_dept_wise(
    db : Session,
    dept_id : str,
    user_log : Users):

    department = db.get(Department , dept_id)
    if department is None :
        logging.error(f"{dept_id} not found error in sort (get) emp/dept")
        raise HTTPException(status_code = 404 , detail = "..Department does'nt exist..")
    
    logging.info(f"Sorting method called by '{user_log.username}'")
    return department.employee_object
    
def get_emp_dept_name(
    db : Session,
    emp_id : str,
    user_log : Users):
    
    employee = db.get(Employee , emp_id)
    if employee is None:
        logging.error(f"{emp_id} not found error in get emp/dept_name ")
        raise HTTPException(status_code = 404 , detail = " Invalid Input , Employee not found " )
    
    dept_id = employee.dept_id
    department = db.get(Department , dept_id)
    logging.info(f"{emp_id} employee department detail by '{user_log.username}'")
    return department

#----------------------------------------------------------

def update_emp(
    db : Session,
    emp_id : str,
    emp : EmployeeSchema,
    background_tasks : BackgroundTasks,
    user_log : Users):

    employee =  db.get(Employee , emp_id)

    if employee is None :
        logging.warning(f"{emp_id} , employee not found while updating ")
        raise HTTPException(status_code = 404 , detail = "User not found for updating the data")
    
    try:
        if employee.e_id != emp.e_id:
            logging.warning("ID altering in update_emp function")
            raise DifferentIDException(employee.e_id,emp.e_id)

    except DifferentIDException as e:
        raise HTTPException(status_code = 409 , detail =" Employee ID can't change during details updatation")

    employee.name = emp.name
    employee.age = emp.age
    employee.dept_id=emp.dept_id
    Department.dept_id = employee.dept_id
    db.commit()
    db.refresh(employee)

    background_tasks.add_task(update_notification , emp_id)

    logging.info(f"{emp_id}, employee updated by user : '{user_log.username}'")
    return employee

#------------------------------------------------------------------------------

def delete_emp(
    db : Session,
    emp_id : str,
    user_log : Users):

    employee = db.get(Employee , emp_id)
    if employee is None:
        logging.warning("employee not found in delete function ")
        raise HTTPException(status_code = 404 , detail = "!! Unable to delete !!..Employee data not found..")

    db.delete(employee)
    db.commit()
    logging.info(f"{emp_id} , employee deleted by '{user_log.username}'")
    return {"message":f"Employee {emp_id} deleted successfully"}