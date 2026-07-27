# # class student:
# #     def __init__(self ,name , age):
# #         self.name = name
# #         self.age  =  age 

# #     def marks(self,subj,marks):
# #         return f"{self.name} has obtained {marks} marks in {subj} at the age of{self.age}"
    

# # std = student("Rahul",22)
# # print(std.marks("phy", 90))
# # print(std)>>> 
# class Car:
#     def __init__(self, color, mileage):
#         self.color = color
#         self.mileage = mileage
#     def __str__(self):
#         return f"The {self.color} car has {self.mileage:,} miles"
#     def __eq__(self,other):
#         return self.mileage == other.mileage

# blue = Car(color="blue", mileage=20_000)
# red = Car(color="red", mileage=30_000)
# print(red,blue)
# print(blue==red)

# # Week 1 , Day 2  
# # Functions , Closures , Decorators , *args , **kwargs

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
        if val <= 0:
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

S_id = input("\nEnter the Name of the student : ")
std_name = input("Enter the ID of the Student : ")

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
            grade_dict[subj] = marks
        return grade_dict

n = int(input("Enter the number of Subjects : "))
subj_obj= Subject(n)
print(subj_obj)
# subj_obj.subj = 4
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











    # @price.deleter
    # def price(self):
    #     print("Deleting ")
    #     del self.price
    
# print("\nWelcome to the Grade Calculator Application Tool (CLI MODE)")

# # Details of Student 
# id_no = input("\nEnter your id :")
# name = input("Enter your name:")

# if name.isnumeric():
#     print("!! Invalid Output!! , Only Letters are allowed in the Name...")

# else:
#     n = int(input("\nEnter the number of subjects: "))

#     if(n == 0):
#         print("!!! Invalid input !!! , Please enter at least one Subject to calculate the average")

#     else:
#         grade_dict = {}
        
#         # Function for Collcting marks
#         @data_collect
#         def data(n):
#             for _ in range(n):
#                 subj = input("Enter subject: ")
#                 marks = int(input("Enter marks between (0-100): ")) 
#                 grade_dict[subj] = marks
#             return grade_dict
#         grade_dict = data(n)

#         # Total and Average using standard python concept
#         @operations
#         def avg(grade_dict):

#             total = sum(grade_dict.values())
#             average = total/n
#             print(f"\nAverage marks by py-methods : {average}")
#             return total , average
#         Total,Avg = avg(grade_dict)

#         @func_time
#         # Total and Average using CLOSURE concept
#         def cls_outer(grade_dict):
#             def cls_inner(marks_total):
#                 marks_total = sum(grade_dict.values())
#                 aver = marks_total/n
#                 return aver
#             return cls_inner
#         closure = cls_outer(grade_dict)    
#         print("\nAverage Marks by Closures :",closure(Total))
        
#         @func_time
#         # Function for Calculating GRADE
#         def grade_func(avg):
#             if avg >= 90 and avg <= 100:
#                 grade = 'AA'
#             elif avg >= 80 and avg < 90:
#                 grade = 'AB'
#             elif avg >= 70 and avg < 80:
#                 grade = 'BB'
#             elif avg >= 60 and avg < 70:
#                 grade = 'BC'
#             elif avg >=50 and avg < 60:
#                 grade = 'CC'
#             else:
#                 grade = 'D'
#             return grade
#         gr = grade_func(Avg)

#         # Rounding the average to 3 decimal points
#         Avg = round(Avg,3)
        
#         # DETAILS func using the Arbitary arguments and Keyword arbitary arguments
#        