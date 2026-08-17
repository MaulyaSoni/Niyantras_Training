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

class UsersSchema(BaseModel):
    # userid : str = Field(nullable = False)
    username : str = Field(min_length = 2)
    password : str = Field(nullable = False)
    # role : str = Field(max_length = 15)

class UsersResponse(BaseModel):
    userid : int
    username : str
    # hashed_password : str
    role : str

    model_config = ConfigDict(from_attributes = True)

class UserIn(BaseModel):
    hashed_password : str


class Token(BaseModel):
    access_token : str
    token_type : str