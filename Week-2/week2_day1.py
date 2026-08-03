from collections import Counter, defaultdict, namedtuple
import csv
import itertools

EmployeeRecordClass = namedtuple(
    "EmployeeRecordClass"
    , 
    ["Employee_ID","Name","Age","Gender","Department","Experience_Years","Salary_USD","Remote_Work","Performance_Score","City"]
    ,
)

emp_list =list(csv.reader(open("tech_company_employee_data_1000.csv","r")))
employee_data_list = [EmployeeRecordClass._make(row) for row in emp_list[1:]]
print("Emp Data Row Wise Representation\n")
print(employee_data_list[1:10])

# Nested Comprehension for the experience employee with the condition of Remotly working 
exp_emp_list = [emp.Name for emp in employee_data_list if emp.Remote_Work == "Yes" if int(emp.Experience_Years) > 5]
print("\nExperienced and Remote employee List..........")
print(exp_emp_list[:10])

sorted_emp = sorted(employee_data_list , key=lambda emp_list: emp_list.Department)
print("\nSorted employees list...........")
print(sorted_emp[:5])

# Grouping Departments 
dept_groupby = itertools.groupby(sorted_emp, key=lambda emp: emp.Department)

city = [emp.City for emp in employee_data_list]
city_counter = Counter(city)
print("\nUsing most_common() method , names of the most common city and its number (how many time it is being repeated)")
print(city_counter.most_common(3))

# Defaultdict for  performance score
performance = defaultdict(list)

for emp in employee_data_list:
    performance[emp.Performance_Score].append(emp.Name)

# print("Number of Employees by Performance Score")
# for score, names in performance.items():
#     print(f"Performance_score {score}: {len(names)} employees")
