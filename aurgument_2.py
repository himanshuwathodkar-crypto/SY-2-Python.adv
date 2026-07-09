def student_details(name, rollno):
    print("Name :", name)
    print("Roll Number:", rollno)
    print()

def course(name, course="B.Tech"):
    print("Student Name :", name)
    print("Course:", course)
    print()

def student_subjects(name, *subjects):
    print("Student Name :", name)
    print("Subjects:", subjects)
    print()

student_details(str(input("Enter your name: ")), int(input("Enter your roll number: ")))

course(str(input("Enter your name: ")), str(input("Enter your course: ")))

n=int(input("Enter the number of subjects: "))
subjects = []
for i in range(n):
    subject = input("Enter subject :")
    subjects.append(subject)
student_subjects(str(input("Enter your name: ")), subjects)