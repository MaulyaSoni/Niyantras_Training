import csv
import logging
from collections import namedtuple
import sys

logging.basicConfig(
    filename="processing_file.log",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

EmployeeRecord = namedtuple(
    "EmployeeRecord",
    [
        "Employee_ID",
        "Name",
        "Age",
        "Gender",
        "Department",
        "Experience_Years",
        "Salary_USD",
        "Remote_Work",
        "Performance_Score",
        "City",
    ],
)

class AgeException(Exception):
    """When employee age is invalid."""
    pass
class NameException(Exception):
    """When employee Name is invalid."""
    pass

def validate_row(row):
    age = int(row[2])
    if age <= 0:
        raise AgeException(f"Invalid Age : {age}")

    name = row[1]
    is_name_contain_digit = any(char.isdigit() for char in name)
    if not name or is_name_contain_digit == True:
        raise NameException(f"Invalid Name : {name}")

def load_employees(file_name):
    employee_list = []
    with open(file_name, "r") as file:
        reader = csv.reader(file)
        next(reader)
        
        for row in reader:
            try:
                validate_row(row)
                employee = EmployeeRecord._make(row)
                employee_list.append(employee)

            except(ValueError,IndexError,AgeException,NameException) as error:
                logging.error(f"Bad Row : {row} and it's following Error : {error}")


    return employee_list
