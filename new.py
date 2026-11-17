students = {}

def add_student():
    roll_no = int(input("Enter roll number: "))
    name = input("Enter student name: ")
    marks = float(input("Enter marks: "))

    students[roll_no] = {
        "name": name,
        "marks": marks
    }

    print("Student added successfully!")

def display_students():
    for roll_no, details in students.items():
        print("\nRoll Number:", roll_no)
        print("Name:", details["name"])
        print("Marks:", details["marks"])

def search_student():
    roll_no = int(input("Enter roll number to search: "))

    if roll_no in students:
        print("Name:", students[roll_no]["name"])
        print("Marks:", students[roll_no]["marks"])
    else:
        print("Student not found!")

while True:
    print("\n1. Add Student")
    print("2. Display Students")
    print("3. Search Student")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        add_student()
    elif choice == 2:
        display_students()
    elif choice == 3:
        search_student()
    elif choice == 4:
        break
    else:
        print("Invalid choice!")