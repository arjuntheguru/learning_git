student_list = []

def create_student():
    users_name = input("Enter your name: ") 
    new_student = {
        "name":users_name,
        "marks":[]
    }

    return new_student

def append_marks(student,marks):       
    student['marks'].append(int(marks))

def calculate_average_mark(student):
    total_marks = sum(student['marks'])
    length = len(student['marks'])
    if length == 0:
        return 0
    avg = total_marks/length    
    return avg

def student_details(student):
    print("Name of the student is: {}".format(student['name']))
    print("Average mark of the student is: {}".format(calculate_average_mark(student)))

def print_student_list(students):
    for i,student in enumerate(students):
        print("ID: {}".format(i))
        print(student_details(student))

def menu():
    selection = input("Enter 'p' to print the student list, "
                 " 's' to add new student, "
                 "  'a' to add mark to a student or "
                 "  'q' to quit.\nEnter your selection: ")
    while selection != 'q':
        if(selection == 'p'):
            print_student_list(student_list)
        elif(selection == 's'):
            student_list.append(create_student())
        elif(selection == 'a'):
            student_id = input("Enter the id to add a mark to: ")
            student = student_list[int(student_id)]
            new_mark = input("Enter the new mark to be added:  ")
            append_marks(student,int(new_mark))

        selection = input("Enter 'p' to print the student list, "
                    " 's' to add new student, "
                    "  'a' to add mark to a student or "
                    "  'q' to quit.\nEnter your selection: ")

menu()