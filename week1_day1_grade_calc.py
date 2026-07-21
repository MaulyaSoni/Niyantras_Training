# Week 1 , Day 1  
print("Welcome to the Grade Calculator Application Tool (CLI MODE)")

grade_dict = {}
student = {}
id = input("Enter your id :")
name = input("Enter your name:")

student[id]=name


n = int(input("\nEnter the number of subjects: "))
for _ in range(n):
    subj = input("Enter subject: ")
    marks = int(input("Enter marks: ")) 
    grade_dict[subj] = marks

# Average 
total = 0

for subj, marks in grade_dict.items(): 
    total += marks  

avg = total / n
print(avg , total)

# Grade Calculation Part
if avg >= 90 and avg <= 100:
   grade = 'Grade AA'
elif avg >= 80 or avg < 90:
    grade = 'Grade  AB'
elif avg >= 70 and avg < 80:
    grade = 'Grade BB'
elif avg >= 60 and avg < 70:
    grade = 'Grade BC'
elif avg >=50 and avg < 60:
    grade = 'Grade CC'
else:
    grade = 'Grade D'


# Concatination of the Dictionaries

student = student | grade_dict
student[avg] = grade

# print(student)

print(f"\n Grand Total of the student {id} {name} is {total} and it's average marks is {avg}\n")