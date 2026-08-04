from reader import load_employees
import sys
import csv

def emp_find():        
    with open("tech_company_employee_data_1000.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        count = 0
        
        for row in reader:
            name = row[1]
            match name :
                case "Emma Martinez":
                    count += 1
      
    print(f"{count} employees found")

# def match_list(data):
#     match data:
#         case {"Name": "Emma Martinez" }:
#             print(f" found ")

if __name__ == "__main__":
    emp_find()
    
    # data = load_employees("tech_company_employee_data_1000.csv")
    # match_list(data)