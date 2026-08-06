from pydantic import BaseModel
from pydantic import PlainValidator , BeforeValidator
from typing import Annotated , Any

def validate_age(age : Any) -> Any:
    if age > 0:
        return age
    else :
        return age

def validate_name(emp_name : str):
    if emp_name.replace(" ", "").isalpha():
        return emp_name
    else:
        return emp_name
 
class Employee(BaseModel):
    emp_id: str
    emp_name : Annotated[str , BeforeValidator(validate_name)]
    age: Annotated[int , BeforeValidator(validate_age)]
    Designation: str | None = None
    address : str | None = None
