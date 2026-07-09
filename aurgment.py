
def student_details(name, roll_no):
    print("Required Arguments")
    print("Name :", name)
    print("Roll Number  :", roll_no)
    print()

def student_course(name, course="B.Tech"):
    print("Default Argument")
    print("Student Name :", name)
    print("Course :", course)
    print()

def student_subjects(name, *subjects):
    print("Variable-Length Arguments")
    print("Student Name :", name)
    print("Subjects     :", subjects)
    print()

student_details("Himanshu", 23)
student_course("Himanshu")                        
student_subjects("Himanshu", "Python", "C")
