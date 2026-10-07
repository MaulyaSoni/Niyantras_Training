import uuid
from sqlalchemy import Uuid 
from pydantic import BaseModel ,Field , ConfigDict 

class DepartmentSchema(BaseModel):
    # dept_id : str = Field(min_length = 4)
    dept_name : str = Field(min_length = 2)

class DepartmentResponse(BaseModel):
    dept_id : uuid.UUID
    dept_name : str

    model_config = ConfigDict(from_attributes = True)
