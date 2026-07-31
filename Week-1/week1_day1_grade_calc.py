# WEEK 1 - DAY 1 - PYTHON 
print("Welcome to the Grade Calculator Application Tool (CLI MODE)")
grade_dict = {}
student = {}
id_no = input("Enter your id :")
name = input("Enter your name:")
student[id_no]=name


n = int(input("\nEnter the number of subjects: "))

if(n == 0):
    print("!!! Invalid input !!! , Please enter at least one Subject to calculate the average")

else:

    for _ in range(n):
        subj = input("Enter subject: ")
        marks = int(input("Enter marks between (0-100) : ")) 
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

    student |= grade_dict

    # print(student)

    print(f"\nDetails of student : {id_no} {name} \nTotal Score : ({total}/{n*100}) \nAverage marks : {round(avg,3)} \nGrade : {grade}\n")
    