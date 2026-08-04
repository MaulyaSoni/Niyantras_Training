from week1_day1_grade_calc import get_int_input , grade_func
def operations(func):
    def wrapper(*args):
        print("\n...Algorithm is running...")
        result = func(*args)
        print(f"\n...Calculations for {func.__name__!r} fucntion is Completed... \n")
        return result
    return wrapper

class Subject:
    def __init__(self , subj):
        self.subj = subj
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
        self._subj = val

class Student:
    def __init__(self, s_id , name , total , avg , grade , n):
        self.s_id = s_id
        self.name = name
        self.total = total
        self.avg = avg
        self.grade = grade
        self.n = n
    
    def res(self):
        return f"\nDetails of student : \n Student_ID : {self.s_id}\n Student Name : {self.name}  \n Total Marks : {self.total}/{self.n*100} \n  Average marks : {self.avg} \n Grade : {self.grade}\n"


class Details:
    def __init__(self):
        pass
        
    @operations
    def data(self,n):
        global flag
        self.n = n 
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

class Calculations:
    def __init__(self):
        pass

    def avg(self,n , grades):
        self.n = n
        self.grades = grades
        total = sum(grades.values())
        average = total/n
        average= round(average,3)
        return total , average



class Rank:
    def __init__(self):
        pass

    def grade_function(self,avg):
        self.avg = avg
        return grade_func(self.avg)

if __name__ == "__main__":
    
    print("\n...Welcome to the Grade Calculator Application Tool (CLI MODE)...")
    
    flag = True
    
    S_id = input("\nEnter the ID of the student : ")
    std_name = input("Enter the Name of the Student : ")

    if std_name.replace(" ", "").isalpha():
        n = get_int_input("\nEnter the number of Subjects : ", "Please enter a whole number for the number of subjects.")
        if n>0:
            subj_obj= Subject(n)

            if flag == True:
                
                det = Details()
                detail_dict = det.data(n)

                calc = Calculations()
                total , average_func = calc.avg(n,grades = detail_dict)

                rnk = Rank()
                grade = rnk.grade_function(average_func)

                stu = Student(S_id , std_name ,total ,average_func , grade,n)
                print(stu.res())

            else:
                print("Marks can be entered only between 0-100")
        else:
            print("Subjects can't be less than Zero or Negative ")
    else:
        print("Name can't be contain any numbers")