from pydantic import BaseModel ,Field ,EmailStr

class EmployeeSchema(BaseModel):
    e_id : str = Field(min_length = 3)
    age : int = Field
    email :EmailStr
