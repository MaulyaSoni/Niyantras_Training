from fastapi import HTTPException

emp_list = []
def create_emp_data(emp):
    for e in emp_list:
        #emp exist condition
        if e.id == emp.id:
            raise HTTPException(status_code = 400 ,details = "...Same name employee already exist...")
        emp_list.append(emp)
        return{"..Employee Created Successfully.."}

def fetch_details(emp):
    for e in emp_list:
        if e.id == emp_id:
            return e

    raise HTTPException(status_code = 400 , details = "...Employee Not Found...")