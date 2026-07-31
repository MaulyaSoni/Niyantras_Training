# Week 1 , Day 2  
# Functions , Closures , Decorators , *args , **kwargs

# timer using Closures
from time import time
def func_time(func):
    def wrap_time(*args):
        t1 = time()
        result = func(*args)
        t2 = time()
        print(f"Time to execute {func.__name__!r} is {(t2-t1):.2f}s\n")
        return result
    return wrap_time

# Closures
def data_collect(func):
    def wrapper(*args) :
        print("Processing and Collecting your Data...")
        result = func(*args)
        print("Data Capturing Part is done")
        return result
    return wrapper

def operations(func):
    def wrapper(*args):
        print("Algorithm is running...")
        result = func(*args)
        print("Calculations Completed ")
        return result
    return wrapper

def end_part(func):
    def wrapper(*args,**kwargs):
        print("..........Final Result..........")
        result = func(*args,**kwargs)
        print(".........THANK YOU !!!..........")
        return result
    return wrapper

print("\nWelcome to the Grade Calculator Application Tool (CLI MODE)")

# Details of Student 
id_no = input("\nEnter your id :")
name = input("Enter your name:")

if name.isnumeric():
    print("!! Invalid Output!! , Only Letters are allowed in the Name...")

else:
    n = int(input("\nEnter the number of subjects: "))

    if(n == 0):
        print("!!! Invalid input !!! , Please enter at least one Subject to calculate the average")

    else:
        grade_dict = {}
        
        # Function for Collcting marks
        @data_collect
        def data(n):
            for _ in range(n):
                subj = input("Enter subject: ")
                marks = int(input("Enter marks between (0-100): ")) 
                grade_dict[subj] = marks
            return grade_dict
        grade_dict = data(n)

        # Total and Average using standard python concept
        @operations
        def avg(grade_dict):

            total = sum(grade_dict.values())
            average = total/n
            print(f"\nAverage marks by py-methods : {average}")
            return total , average
        Total,Avg = avg(grade_dict)

        @func_time
        # Total and Average using CLOSURE concept
        def cls_outer(grade_dict):
            def cls_inner(marks_total):
                marks_total = sum(grade_dict.values())
                aver = marks_total/n
                return aver
            return cls_inner
        closure = cls_outer(grade_dict)    
        print("\nAverage Marks by Closures :",closure(Total))
        
        @func_time
        # Function for Calculating GRADE
        def grade_func(avg):
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
        gr = grade_func(Avg)

        # Rounding the average to 3 decimal points
        Avg = round(Avg,3)
        
        # DETAILS func using the Arbitary arguments and Keyword arbitary arguments
        @end_part
        def details(*args, **kwargs):
            print(f"\nDetails of student : {id_no} {name} \nTotal Score : ({Total}/{n*100}) \nAverage marks : {Avg} \nGrade : {gr}\n")
        
        details(Avg , Total ,gr,  id = id , name = name)