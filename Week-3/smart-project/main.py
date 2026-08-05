from fastapi import FastAPI
from enum import Enum

class Role(str, Enum):
    Software_Developer = "Software_Developer"
    Quality_Assurance = "Quality_Assurance"
    Software_Architect = "Software_Architect"

app = FastAPI()

@app.get("/user/{username}/roles/{role_name}")
async def get_role(role_name : Role , username :str):
    if role_name is Role.Software_Developer:
        return {username : f"The {role_name}, who builts the software according to the client requirements"}
    elif role_name is Role.Quality_Assurance:
        return {username : f"The {role_name}, who test the software and found the important mistakes that misses by a developer"}
    elif role_name is Role.Software_Architect:
        return {username : f"The {role_name} , who builts the gather requirements and built the pathway and desgin the system"}
    return{role_name , "Based on user , No role found"}

@app.get("/user/{username}")
async def state_role(username : str):
    if username == "Steve Jobs": 
        return {username :"The Tech Genius , Launch Iphone with a great vision"}
    if username == "Sundar Pichai":
        return {username :"The Genius ,  Become the world's biggest and greatest company's CEO"}
    
@app.get("/user/{username}/{age}")
def fetch_username(username :str , age : int):
    return { "The Details we get is of ":username ,"and age of them is": age}

@app.get("/user/{username}/pay_per_day={pay_per_day}/present_days={present_days}")
def calc_salary(username:str , pay_per_day : int , present_days : int):
    if pay_per_day < 0:
        raise Exception("Pay can't be in negative") 
    final_amt = pay_per_day * present_days
    return {"Your Salary for this month is":final_amt}