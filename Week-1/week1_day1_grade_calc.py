# WEEK 1 - DAY 1 - PYTHON 
print("Welcome to the Grade Calculator Application Tool (CLI MODE)")
grade_dict = {}
student = {}

def get_int_input(msg, error_msg):
    while True:
        try:
            return int(input(msg))
        except ValueError:
            print(error_msg)

id_no = input("Enter your id :")
name = input("Enter your name:")
student[id_no]=name


n = get_int_input("\nEnter the number of subjects: ", "Please enter a whole number for the number of subjects.")

if(n == 0):
    print("!!! Invalid input !!! , Please enter at least one Subject to calculate the average")

else:

    for _ in range(n):
        subj = input("Enter subject: ")
        while True:
            marks = get_int_input("Enter marks between (0-100) : ", "Please enter a whole number for marks.")
            if 0 <= marks <= 100:
                break
            print("!!! Invalid input !!! , Please enter marks between 0-100")
        grade_dict[subj] = marks
        
    # Average 
    total = 0

    for subj, marks in grade_dict.items(): 
        total += marks  

    avg = total / n
    # print(f"Your total score is {total} & average score is {avg}")

    # Grade Calculation Part
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


    # Concatination of the Dictionaries

    # print(student)

    print(f"\nDetails of student : {id_no} {name} \nTotal Score : ({total}/{n*100}) \nAverage marks : {round(avg,3)} \nGrade : {grade}\n")
    