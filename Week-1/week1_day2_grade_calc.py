from time import time
from week1_day1_grade_calc import get_int_input , grade_func

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

@data_collect
def data(n):
    grade_dict = {}
    for _ in range(n):
        subj = input("Enter subject: ")
        while True:
            marks = get_int_input("Enter marks between (0-100): ", "!! Invalid Input !! ......Please enter a whole number for marks.")
            if 0 <= marks <= 100:
                break
            print("!!! Invalid input !!! , Please enter marks between 0-100")
        grade_dict[subj] = marks
    return grade_dict

 # Total and Average using standard python concept
@operations
def avg(grade_dict):

    total = sum(grade_dict.values())
    average = total/n
    print(f"\nAverage marks by py-methods : {average}")
    return total , average

@func_time
# Total and Average using CLOSURE concept
def cls_outer(grade_dict):
    def cls_inner(marks_total):
        aver = marks_total/n
        return aver
    return cls_inner


@end_part
def details(*args, **kwargs):
    print(f"\nDetails of student : {id_no} {name} \nTotal Score : ({Total}/{n*100}) \nAverage marks : {Avg} \nGrade : {gr}\n")

if __name__ == "__main__":
    
    print("\nWelcome to the Grade Calculator Application Tool (CLI MODE)")
 
    id_no = input("\nEnter your id :")
    name = input("Enter your name:")

    if not name.replace(" ", "").isalpha():
        print("!! Invalid Output!! , Only Letters are allowed in the Name...")

    else:
        n = get_int_input("\nEnter the number of subjects: ", "Please enter a whole number for the number of subjects.")
        if(n == 0):
            print("!!! Invalid input !!! , Please enter at least one Subject to calculate the average")

        else: 
            grade_dict = data(n)
        
            Total,Avg = avg(grade_dict)
            
            closure = cls_outer(grade_dict)    
            print("\nAverage Marks by Closures :",closure(Total))  
            
            gr = grade_func(Avg)

            # Rounding the average to 3 decimal points
            Avg = round(Avg,3)
            
            # DETAILS func using the Arbitary arguments and Keyword arbitary arguments
            
            details(Avg , Total ,gr, student_id = id_no, name = name)