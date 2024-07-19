# In this service we are implementing CRUD function in dictionary!!!

student = {

}

def add_student_list(name, grade):
    student[name] = grade
    print(f"Added {name} with a {grade}")

def update_student(name, grade):

    if name in student:
        student[name] = grade
        print(f"\n{name} with marks {grade} updated!!\n")

    else:
        print(f"{name} not fund in list.\n")

def delete_student(name):
    if name in student:
        del student[name]
        print(f"\n{name} has been removed from list\n")

    else:
        print(f"\n{name} not found!!!\n")

def view_student():
    if student:
        for name, grade in student.items():
            print(f"\n{name} : {grade}\n")
    else:
        print("\nStudents not found\n")

def main():

    while True:

        print("**********************************")

        print(' Student Managenet System - (SMS) ')
        print("**********************************")
        print()
        print("1. Add Student\n2. Update Details\n3. Delete Student\n4. Display all Student\n5. Exit")
        choice = int(input("Hello, What would you like to do? \n"))

        if choice == 1:
            name = str(input("Enter the name of student: "))
            grade = int(input(f"Enter the grade for {name}: "))
            add_student_list(name, grade)
        elif choice == 2:
            name = str(input("Enter the Updated name of student: "))
            grade = int(input(f"Enter the grade for {name}: "))
        elif choice == 3:
            name = str(input("Enter the name of student need to be removed: "))
            delete_student(name)
        elif choice == 4:
            view_student()
        elif choice == 5:
            print("!!! Good Bye !!!")
            break
        else:
            print("Please enter the correct option")

if __name__ == "__main__":
    main()

