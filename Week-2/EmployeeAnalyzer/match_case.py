import csv

def emp_find(target_name):        
    with open("tech_company_employee_data_1000.csv", "r") as file:
        reader = csv.reader(file)
        next(reader)
        count = 0
        
        for row in reader:
            name = row[1]
            match name:
                case value if value == target_name:
                    count += 1
      
    print(f"{count} employees found for {target_name}")

if __name__ == "__main__":
    emp_find(input("Enter employee name to search: "))
    
    # data = load_employees("tech_company_employee_data_1000.csv")
    # match_list(data)