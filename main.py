from prettytable import  PrettyTable
from students_data import roll, student
from logo import logo2,logo3,logo

#--------------------Printing Logo First--------------------
print(logo)
print(logo3)

#-------------------Printing All Students-------------------
def all_students():
    table = PrettyTable()
    table.add_column('Student Name', student)
    table.add_column('University Roll', roll)

    print(table)

all_students()

#---------------Check students or not-------------------
student_roll = int(input("Enter your roll number : "))

def verify_students(roll_number):
    if roll_number not in roll:
        return  False

if verify_students(student_roll) == False :
    print("Your name isn't in class list.Register yourself.\nContact to the Administration!")

#---------------Collecting Attendence--------------------
present_students = []


