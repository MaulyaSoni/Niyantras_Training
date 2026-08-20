from pydantic import BaseModel ,Field , ConfigDict 

class EmployeeSchema(BaseModel):
    e_id : str = Field(min_length = 4)
    name : str = Field(max_length = 25)
    age : int = Field(gt = 0) #greater than 0
    dept_id : str = Field(min_length = 4)
    
class EmployeeResponse(BaseModel):
    e_id : str
    name : str
    age : int 
    dept_id : str
    
    # for fetching data , setting the rule to read from the database with the help of ConfigDict
    model_config = ConfigDict(from_attributes = True)
