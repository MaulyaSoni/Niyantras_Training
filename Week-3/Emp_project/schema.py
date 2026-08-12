from pydantic import BaseModel ,Field , ConfigDict 

class DepartmentSchema(BaseModel):
    dept_id : str = Field(min_length = 3)
    dept_name : str = Field(min_length = 1)


class DepartmentResponse(BaseModel):
    dept_id : str
    dept_name : str

    model_config = ConfigDict(from_attributes = True)


class EmployeeSchema(BaseModel):
    e_id : str = Field(min_length = 4)
    name : str = Field(max_length = 25)
    age : int = Field(gt = 0) #greater than 0
    dept_id : str = Field(nullable = False)


class EmployeeResponse(BaseModel):
    e_id : str
    name : str
    age : int 
    dept_id : str

    # for fetching data , setting the rule to read from the database with the help of ConfigDict
    model_config = ConfigDict(from_attributes = True)