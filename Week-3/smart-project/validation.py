from typing import Annotated, Any
from pydantic import BaseModel

def validate_age(age : Any) -> Any:
    if age > 0:
        return age
    else :
        return age

class Student(BaseModel):
    name : str
    age : Annotated[int , PlainValidator(validate_age)]

print(Student(age = 80))
print(Student(age = -1)) 