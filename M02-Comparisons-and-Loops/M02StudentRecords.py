# Edward Schaefer
# M02StudentRecords.py
# This program will take a student last name and first name
# and will ask for a GPA value for this student.
# Depending on the GPA value, the program will then print a
# Dean's List message, an Honor Roll message, or nothing.
# Program will be terminated if student last name ZZZ is entered
# Variables included:
# studentlast- a string used to store a student's last name
# studentfirst- a string used to store a student's first name
# gpa- float used to store a student's gpa

while True:
    # ask for last name
    print("Please enter the student's last name: ")
    studentlast = input()

    # check for exit code
    if studentlast == 'ZZZ':
        print("Goodbye!")
        break

    # ask for first name
    print("Please enter the student's first name: ")
    studentfirst = input()

    # ask for GPA
    print("Please enter the student's GPA: ")
    gpa = float(input())

    # check GPA against dean's list/honor roll thresholds
    if gpa >= 3.5:
        print(f"{studentfirst} {studentlast} has made the Dean's List!\n")
    elif gpa < 3.5 and gpa >= 3.25:
        print(f"{studentfirst} {studentlast} has made the Honor Roll!\n")
