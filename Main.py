# Student Grade Calculator

students = {}  # Dictionary to store student data


def add_student():
    name = input("Enter student name: ").title()
    subjects = {}
    n = int(input("Enter number of subjects: "))
    
    for _ in range(n):
        subject = input("Enter subject name: ").title()
        marks = float(input(f"Enter marks for {subject}: "))
        subjects[subject] = marks

    students[name] = subjects
    print(f"{name}'s record added successfully.\n")


def calculate_average(marks_dict):
    total = sum(marks_dict.values())
    return total / len(marks_dict)


def assign_grade(average):
    if average >= 90:
        return "A+"
    elif average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 50:
        return "D"
    else:
        return "F"


def display_all():
    if not students:
        print("No student records found.\n")
        return

    for name, marks in students.items():
        average = calculate_average(marks)
        grade = assign_grade(average)
        print(f"\nStudent Name: {name}")
        for subject, mark in marks.items():
            print(f"  {subject}: {mark}")
        print(f"  Average: {average:.2f}")
        print(f"  Grade: {grade}")
    print()


def menu():
    while True:
        print("=== Student Grade Calculator ===")
        print("1. Add Student")
        print("2. Display All Records")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            display_all()
        elif choice == "3":
            print("Thank you for using the system.")
            break
        else:
            print("Invalid choice. Please try again.\n")


# Run the program
menu()
