from enum import Enum
from fastapi import FastAPI , HTTPException
from pydantic import BaseModel , BeforeValidator , PlainValidator


# Pydantic Models 
# Model creation for get (read)
class Role(str, Enum):
    Software_Developer = "Software_Developer"
    Quality_Assurance = "Quality_Assurance"
    Software_Architect = "Software_Architect"

# Model Creation for post (create)
class Employee(BaseModel):
    name: str
    age: int
    Designation: str
    desc: str | None = None

class Item(BaseModel):
    item_name: str
    item_price: int

app = FastAPI()

@app.post("/items/")
def create_item(item :Item):
    return item

@app.get("/user/{username}/salary/details")
def calc_salary(username:str , pay_per_day : int , present_days : int):

    if pay_per_day < 0:
        raise HTTPException(status_code = 400 , detail= "Pay value can't be in negative")
   
    if present_days < 0:
        raise HTTPException(status_code = 400 , detail= "Days can't be  negative")      
   
    final_amt = pay_per_day * present_days
    return {"Your Salary for this month is":final_amt , "Pay per day " :pay_per_day , "present_days":present_days}

@app.get("/user/{username}/ceos")
async def state_role(username : str):

    if username == "Steve Jobs": 
        return {username :"The Tech Genius , Launch Iphone with a great vision"}
    
    if username == "Sundar Pichai":
        return {username :"The Genius ,  Become the world's biggest and greatest company's CEO"}

@app.get("/user/{username}/roles/{role_name}")
async def get_role(role_name : Role , username :str):
    
    if role_name is Role.Software_Developer:
        return {username : f"The {role_name}, who builts the software according to the client requirements"}
    
    elif role_name is Role.Quality_Assurance:
        return {username : f"The {role_name}, who test the software and found the important mistakes that misses by a developer"}
    
    elif role_name is Role.Software_Architect:
        return {username : f"The {role_name} , who builts the gather requirements and built the pathway and desgin the system"}
    
    return{role_name , "Based on user , No role found"}

@app.get("/user/{username}/{age}")
def fetch_username(username :str , age : int):
    return { "The Details we get is of ":username ,"and age of them is": age}

@app.get("/")
def welcome():
    return {"Welcome to the server"}