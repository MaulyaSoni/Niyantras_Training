from week1_day1_grade_calc import get_int
from abc import ABC  , abstractmethod
from dataclasses import dataclass

@dataclass
class StudentDetails():
    s_id : str
    std_name : str
    n : int

    def card(self):
        return self.s_id , self.std_name , self.n

s_id = input("\nEnter the ID of the student : ")
std_name = input("Enter the Name of the Student : ")    
n = get_int_input("Enter the Number of Subjects : ", "Please enter a whole number for the number of subjects.")

st = StudentDetails(s_id=s_id,std_name=std_name,n=n)
s_id , std_name , n = st.card()

class Student(ABC):
    def __init__(self, s_id , name ):
        self.s_id = s_id
        self.name = name

    @abstractmethod 
    def data(self):
        pass    

# Composite Class 1 
class MarksDetails(Student):
    def __init__(self):
        print("\nMarksDetails Class object created ")

    def data(self,n:int):
        self.n = n 
        # global flag
        grade_dict={}
        for _ in range(n):
            subj = input("\nEnter name of the Subject : ")
            while True:
                marks = get_int_input("Enter marks between (0-100): ", "Please enter a whole number for marks.")
                if 0 <= marks <= 100:
                    grade_dict[subj] = marks
                    break
                print("Marks can be entered only between 0-100")
                        
        return grade_dict

# Composite Class 2
class Calculations:
    def __init__(self):
        self.det = MarksDetails()
        print("\nDetails class object created")

    def avg(self,n):
        self.n = n
        grades = self.det.data(n)
     
        total = sum(grades.values())
        average = total/n
        average= round(average,3)
        
        return total , average

class Rank:
    def __init__(self):
        print("\nRank class object created")

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

class Result:
    def __init__(self,s_id,name,avg,grade,t_marks,n):
        print("\n.....Printing your result......")
        self.s_id=s_id
        self.name = name
        self.avg = avg
        self.grade  = grade
        self.t_marks = t_marks
        self.n = n       

    def res_func(self):
        return f"\n Details of student : \n Student ID : {self.s_id}\n Student Name : {self.name}  \n Total Marks :{self.t_marks}/{self.n*100} \n Average marks : {self.avg} \n Grade : {self.grade}\n"


flag = True 

if std_name.replace(" ", "").isalpha() and n>0: # isalpha() 
   
    cal_obj= Calculations()
    t_marks , avg = cal_obj.avg(n)
    
    rnk= Rank()
    gr = rnk.grade_func(avg)

    res = Result(s_id,std_name,avg,gr,t_marks,n)
    print(res.res_func())

else:
    print("Name can't be contain any numbers or Subjects can't be less than Zero or can't be Negative")