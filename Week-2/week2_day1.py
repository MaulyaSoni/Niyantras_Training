from collections import Counter, defaultdict, namedtuple
import csv
import itertools

EmployeeRecordClass = namedtuple(
    "EmployeeRecordClass"
    , 
    ["Employee_ID","Name","Age","Gender","Department","Experience_Years","Salary_USD","Remote_Work","Performance_Score","City"]
    ,
)

with open("tech_company_employee_data_1000.csv", "r", newline="") as file:
    emp_list = list(csv.reader(file))

employee_data_list = []
for row in emp_list[1:]:
    if len(row) == 10:
        employee_data_list.append(EmployeeRecordClass._make(row))
print("Emp Data Row Wise Representation\n")
print(employee_data_list[1:10])

# Nested Comprehension for the experience employee with the condition of Remotly working 
exp_emp_list = []
for emp in employee_data_list:
    try:
        experience_years = int(emp.Experience_Years)
        if emp.Remote_Work == "Yes" and experience_years > 5:
            exp_emp_list.append(emp.Name)
    except ValueError:
        continue
print("\nExperienced and Remote employee List..........")
print(exp_emp_list[:10])

sorted_emp = sorted(employee_data_list , key=lambda employee: employee.Department)
print("\nSorted employees list...........")
print(sorted_emp[:5])

# Grouping Departments 
dept_groupby = {
    department: list(group)
    for department, group in itertools.groupby(sorted_emp, key=lambda employee: employee.Department)
}

print("\nEmployees grouped by department")
for department, employees in dept_groupby.items():
    print(f"{department}: {len(employees)} employees")

city = [emp.City for emp in employee_data_list]
city_counter = Counter(city)
print("\nUsing most_common() method , names of the most common city and its number (how many time it is being repeated)")
print(city_counter.most_common(3))

# Defaultdict for  performance score
performance = defaultdict(list)

for emp in employee_data_list:
    performance[emp.Performance_Score].append(emp.Name)

print("\nNumber of Employees by Performance Score")
for score, names in performance.items():
    print(f"Performance_score {score}: {len(names)} employees , {type(names)}")
