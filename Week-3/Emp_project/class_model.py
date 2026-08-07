from pydantic import BaseModel
from pydantic import PlainValidator , BeforeValidator
from typing import Annotated , Any

def validate_age(age : Any) -> Any:
    if age > 0:
        return age
    else :
        return age

def validate_name(name : str):
    if name.replace(" ", "").isalpha():
        return name
    else:
        return name
 
class Employee(BaseModel):
    e_id: str
    name : Annotated[str , BeforeValidator(validate_name)]
    age: Annotated[int , BeforeValidator(validate_age)]
  