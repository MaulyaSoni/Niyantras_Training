from abc import ABC  , abstractmethod
from week1_day1_grade_calc import get_int_input , grade_func

class StudentDetails:
    def __init__(self):
        print("\n...Welcome to the Grade Calculator Application Tool (CLI MODE)...")
    def card(self):
        s_id = input("\nEnter the ID of the student : ")
        std_name = input("Enter the Name of the Student : ")
        return s_id , std_name

# Abstract Class 
class Student(ABC):
    def __init__(self, s_id , name ):
        self.s_id = s_id
        self.name = name

    @abstractmethod 
    def data(self):
        pass    

# Composite Class 1 
class MarksDetails(Student):
    def __init__(self, s_id="", name=""):
        super().__init__(s_id, name)
        print("MarksDetails Class object created ")

    def data(self,n):
        self.n = n 
        global flag
        grade_dict={}
        for _ in range(n):
            subj = input("\nEnter name of the Subject : ")
            while True:
                marks = get_int_input("Enter marks between (0-100): ", "!! Invalid Input !! ......Please enter a whole number for marks.")
                if 0 <= marks <= 100:
                    break
                print("Marks can be entered only between 0-100")
            grade_dict[subj] = marks
        
        return grade_dict

# Composite Class 2
class Calculations:
    def __init__(self):
        #object of MarksDetails class
        self.det = MarksDetails()
        print("Details class object created")

    def avg(self,n):
        #Composition instance calling
        grades = self.det.data(n)
        self.n = n
     
        total = sum(grades.values())
        average = total/n
        average= round(average,3)
        
        return total , average


# Composite class 3
class Rank:
    def __init__(self):
        print("Rank class object created")

    def grade_function(self, avg):
        grade =''
        self.avg = avg
        return grade_func(self.avg)

class Result:
    def __init__(self,s_id,name,avg,grade,t_marks,n):
        print("\n.....Printing your result......")
        self.s_id=s_id
        self.name = name
        self.avg = avg
        self.grade  = grade
        self.t_marks = t_marks
        self.n = n           
    def __str__(self):
        return f"\n Details of student : \n Student ID : {self.s_id}\n Student Name : {self.name}  \n Total Marks :{self.t_marks}/{self.n*100} \n Average marks : {self.avg} \n Grade : {self.grade}\n"

if __name__ == "__main__":

    flag = True 
    sd = StudentDetails()
    s_id , std_name = sd.card()


    if std_name.replace(" ", "").isalpha():
        # number of subject condition 
        n = get_int_input("Enter the Number of Subjects : ", "Please enter a whole number for the number of subjects.")
        if n>0:
            cal_obj= Calculations()
            t_marks , avg = cal_obj.avg(n)

            # marks negavtive condition
            if flag == True:
                rnk= Rank()
                gr = rnk.grade_function(avg)

                res = Result(s_id,std_name,avg,gr,t_marks,n)
                print(res)

            else:
                print("Marks can be entered only between 0-100")
        else:
            print("Subjects can't be less than Zero or can't be Negative ")
    else:
        print("Name can't be contain any numbers")


# Note :
# Why choose the Composition over the Inheritance ?
# By choosing the composite class you can do complex task with less brainstoming by having a class in another class by defining the instances in that class.
# By this the maintainence of the code increases , and class hierarchical complexity decreases.
# It gives you flexibility to resolve major code changes by changing less lines of code , along with reusability we are getting , which helps us to use at any part of code without making the inheritance and complex codes.
# When an object or the thing need other's behaviour for making the simple way to the output with less complexity and maintanence , they use the Composite Classes.   
