from pydantic import BaseModel ,Field , ConfigDict 

class EmployeeSalary(BaseModel):
    e_id : str
    present_days : int = Field(gt = 0)
    salary : int = Field(gt = 0 , nullable = False)

class EmployeeSchema(BaseModel):
    e_id : str = Field(min_length = 3)
    name : str = Field(max_length = 25)
    age : int = Field(gt = 0) #greater than 0

class EmployeeResponse(BaseModel):
    e_id : str
    name : str
    age : int 

    # for fetching data , setting the rule to read from the database with the help of ConfigDict
    model_config = ConfigDict(from_attributes = True)
