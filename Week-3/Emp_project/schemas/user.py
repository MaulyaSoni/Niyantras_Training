from pydantic import BaseModel ,Field , ConfigDict 

class UsersSchema(BaseModel):
    username : str = Field(min_length = 2)
    password : str = Field(min_length = 6)
    # admin_key : str | None = None

class UsersResponse(BaseModel):
    userid : int
    username : str
    user_role : str

    model_config = ConfigDict(from_attributes = True)
