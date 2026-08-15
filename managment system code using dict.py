students = {}

while True:
    print("\n========== STUDENT MANAGEMENT SYSTEM ==========")
    print("1. Add Student")
    print("2. Display All Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Calculate Topper")
    print("7. Display Passed Students")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    # 1. Add Student
    if choice == 1:
        roll_no = input("Enter Roll Number: ")

        if roll_no in students:
            print("Student already exists!")
        else:
            name = input("Enter Student Name: ")
            branch = input("Enter Branch: ")

            python = float(input("Enter Python marks: "))
            maths = float(input("Enter Maths marks: "))
            english = float(input("Enter English marks: "))

            total = python + maths + english
            average = total / 3

            if average >= 90:
                grade = "A+"
            elif average >= 80:
                grade = "A"
            elif average >= 70:
                grade = "B"
            elif average >= 60:
                grade = "C"
            elif average >= 50:
                grade = "D"
            else:
                grade = "F"

            students[roll_no] = {
                "name": name,
                "branch": branch,
                "python": python,
                "maths": maths,
                "english": english,
                "total": total,
                "average": average,
                "grade": grade
            }

            print("Student added successfully!")


    # 2. Display All Students
    elif choice == 2:

        if len(students) == 0:
            print("No students found!")

        else:
            print("\n---------- ALL STUDENTS ----------")

            for roll_no, details in students.items():
                print("\nRoll Number :", roll_no)
                print("Name        :", details["name"])
                print("Branch      :", details["branch"])
                print("Python      :", details["python"])
                print("Maths       :", details["maths"])
                print("English     :", details["english"])
                print("Total       :", details["total"])
                print("Average     :", round(details["average"], 2))
                print("Grade       :", details["grade"])


    # 3. Search Student
    elif choice == 3:

        roll_no = input("Enter Roll Number to search: ")

        if roll_no in students:
            details = students[roll_no]

            print("\nStudent Found!")
            print("Name     :", details["name"])
            print("Branch   :", details["branch"])
            print("Total    :", details["total"])
            print("Average  :", round(details["average"], 2))
            print("Grade    :", details["grade"])

        else:
            print("Student not found!")


    # 4. Update Student
    elif choice == 4:

        roll_no = input("Enter Roll Number to update: ")

        if roll_no in students:

            new_name = input("Enter new name: ")
            new_branch = input("Enter new branch: ")

            students[roll_no]["name"] = new_name
            students[roll_no]["branch"] = new_branch

            print("Student details updated!")

        else:
            print("Student not found!")


    # 5. Delete Student
    elif choice == 5:

        roll_no = input("Enter Roll Number to delete: ")

        if roll_no in students:
            del students[roll_no]
            print("Student deleted successfully!")

        else:
            print("Student not found!")


    # 6. Find Topper
    elif choice == 6:

        if len(students) == 0:
            print("No students available!")

        else:
            topper_roll = max(
                students,
                key=lambda roll: students[roll]["average"]
            )

            topper = students[topper_roll]

            print("\n========== TOPPER ==========")
            print("Roll Number :", topper_roll)
            print("Name        :", topper["name"])
            print("Average     :", round(topper["average"], 2))
            print("Grade       :", topper["grade"])


    # 7. Display Passed Students
    elif choice == 7:

        print("\n---------- PASSED STUDENTS ----------")

        found = False

        for roll_no, details in students.items():

            if details["average"] >= 40:
                print(
                    roll_no,
                    "-",
                    details["name"],
                    "-",
                    round(details["average"], 2)
                )
                found = True

        if found == False:
            print("No passed students found!")


    # 8. Exit
    elif choice == 8:

        print("Thank you for using Student Management System!")
        break

    else:
        print("Invalid choice! Please try again.")