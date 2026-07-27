# # timer using Closures
# from time import time
# def func_time(func):
#     def wrap_time(*args):
#         t1 = time()
#         result = func(*args)
#         t2 = time()
#         print(f"Time to execute {func.__name__!r} is {(t2-t1):.2f}s\n")
#         return result
#     return wrap_time

# # Closures
# def data_collect(func):
#     def wrapper(*args) :
#         print("Processing and Collecting your Data...")
#         result = func(*args)
#         print("Data Capturing Part is done")
#         return result
#     return wrapper

def operations(func):
    def wrapper(*args):
        print("\n...Algorithm is running...")
        result = func(*args)
        print(f"\n...Calculations for {func.__name__!r} fucntion is Completed... \n")
        return result
    return wrapper

# def end_part(func):
#     def wrapper(*args,**kwargs):
#         print("..........Final Result..........")
#         result = func(*args,**kwargs)
#         print(".........THANK YOU !!!..........")
#         return result
#     return wrapper

print("\n...Welcome to the Grade Calculator Application Tool (CLI MODE)...")

# Property concept for validating the subject
class Subject:
    def __init__(self , subj):
        self._subj = subj
    @property
    #Getter method 
    def subj(self):
        print("Fetching subj")
        return self._subj
    
    #Setter method  
    @subj.setter
    def subj(self,val):
        print("\n Validating number of subjects ")
        if val == 0 :
            raise ValueError("\n Subjects can't be zero or negative \n")
        self._subj

class Student:
    #Function will execute at last when to show the full detail of Students
    def __init__(self, s_id , name , avg , grade):
        self.s_id = s_id
        self.name = name
        self.avg = avg
        self.grade = grade
    
    def __str__(self):
        return f"\nDetails of student : \n Student_ID : {self.s_id}\n Student Name : {self.name}  \n  Average marks : {self.avg} \n Grade : {self.grade}\n"

flag = True
class Details:
    def __init__(self):
        pass
        
    @operations
    def data(self,n):
        self.n = n 
        grade_dict={}
        for _ in range(n):
            subj = input("\nEnter name of the Subject : ")
            marks = int(input("Enter marks between (0-100): "))
            if marks > 100 or marks < 0:
                flag = False
                break 
            grade_dict[subj] = marks
        return grade_dict

S_id = input("\nEnter the ID of the student : ")
std_name = input("Enter the Name of the Student : ")
if not std_name.isnumeric():

    n = int(input("Enter the number of Subjects : "))
    if n>0:
        subj_obj= Subject(n)

        print(subj_obj)
        # subj_obj.subj = 4
        if flag == True:
            det = Details()
            detail_dict = det.data(n)

            class Calculations:
                def __init__(self):
                    pass
                
                def avg(self,n , grades):
                    self.n = n
                    self.grades = grades
                    total = sum(grades.values())
                    average = total/n
                    average= round(average,3)
                    # print(f"After avg {average}")
                    return average

            calc = Calculations()
            average_func = calc.avg(n,grades = detail_dict)

            class Rank:
                def __init__(self):
                    pass
                # Function for Calculating GRADE
                def grade_func(self,avg):
                    self.avg = avg
                    grade =''

                    if avg >= 90 and avg <= 100:
                        grade = 'AA'
                    elif avg >= 80 and avg < 90:
                        grade = 'AB'
                    elif avg >= 70 and avg < 80:
                        grade = 'BB'
                    elif avg >= 60 and avg < 70:
                        grade = 'BC'
                    elif avg >=50 and avg < 60:
                        grade = 'CC'
                    else:
                        grade = 'D'
                    return grade

                # Rounding the average to 3 decimal points
            rnk = Rank()
            grade = rnk.grade_func(average_func)

            # STUDENT Class object calling 
            stu = Student(S_id , std_name ,average_func , grade)
            print(stu)
        else :
            print("Marks can be entered only between 0-100")
    else:
        print("Subjects can't be less than Zero or Negative ")
else:
    print("Name can't be contain any numbers")