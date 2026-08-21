import os
import logging
from sqlalchemy.orm import Session
from fastapi import HTTPException , Depends ,  Request , BackgroundTasks
from models.model import Users , Department
from schemas.department import DepartmentSchema , DepartmentResponse 
from operations.exceptions import DataCannotInsertException , datacannotinsert_exception_handler
from operations.exceptions import InvalidEmpIDException , invalid_id_exception_handler 
from operations.exceptions import DifferentIDException , different_id_exception_handler

logging.basicConfig(
    filename="Log_employee_project.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

#----------------------------------------------------------

def create_dept(
    db : Session,
    dept : DepartmentSchema,
    user_log : Users):

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
    logging.info(f"{dept.dept_id} , New Department created by '{user_log.username}'")
    return department

#----------------------------------------------------------

def fetch_dept(
    db : Session,
    user_log : Users):
    
    logging.info(f"Fetching all department details by '{user_log.username}'")
    return db.query(Department).all()

#----------------------------------------------------------

def delete_dept(
    db:Session,
    dept_id : str,
    user_log : Users):

    department = db.get(Department , dept_id)
    if department is None :
        logging.error(f"{dept_id} not found error in sort (get) emp/dept")
        raise HTTPException(status_code = 404 , detail = "..Department does'nt exist..")
   
    if department.employee_object:
        logging.error(f"trying to delete Department containing emp")
        raise HTTPException(status_code = 403 , detail = "can't delete , the department contains employee ")
    
    db.delete(department)
    db.commit()
    logging.info(f"{dept_id}, department deleted by '{user_log.username}'")
    return {"message": f"{dept_id} , department deleted successfully"}
