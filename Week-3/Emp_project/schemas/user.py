import uuid
from sqlalchemy import UUID
from pydantic import BaseModel ,Field , ConfigDict 

class UsersSchema(BaseModel):
    username : str = Field(min_length = 2)
    password : str = Field(min_length = 6)
  
class UsersResponse(BaseModel):
    userid : uuid.UUID
    username : str
    user_role : str

    model_config = ConfigDict(from_attributes = True)
