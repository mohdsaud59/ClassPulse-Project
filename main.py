# Student Performance Analytics System - Phone Friendly
# Runs in normal Python online compilers. No extra libraries required.

students = [
    {"name":"Aman","marks":82,"attendance":91},
    {"name":"Rahul","marks":74,"attendance":86},
    {"name":"Priya","marks":91,"attendance":95},
    {"name":"Neha","marks":68,"attendance":78},
    {"name":"Rohit","marks":59,"attendance":72},
    {"name":"Simran","marks":88,"attendance":93},
    {"name":"Vikas","marks":77,"attendance":84},
    {"name":"Anjali","marks":95,"attendance":97},
    {"name":"Karan","marks":63,"attendance":75},
    {"name":"Pooja","marks":81,"attendance":89},
]

def grade(marks):
    if marks >= 90: return "A+"
    if marks >= 80: return "A"
    if marks >= 70: return "B"
    if marks >= 60: return "C"
    if marks >= 50: return "D"
    return "F"

def show_all():
    print("\n--- ALL STUDENTS ---")
    for i, s in enumerate(students, 1):
        print(f"{i}. {s['name']:10} Marks: {s['marks']:3}  Attendance: {s['attendance']:3}%  Grade: {grade(s['marks'])}")

def dashboard():
    avg_marks = sum(s["marks"] for s in students) / len(students)
    avg_att = sum(s["attendance"] for s in students) / len(students)
    passed = sum(s["marks"] >= 50 for s in students)
    pass_rate = passed / len(students) * 100

    print("\n===== PERFORMANCE DASHBOARD =====")
    print("Total Students :", len(students))
    print(f"Average Marks  : {avg_marks:.2f}")
    print(f"Average Attend. : {avg_att:.2f}%")
    print(f"Pass Rate      : {pass_rate:.2f}%")

def top_students():
    print("\n--- TOP 5 STUDENTS ---")
    for i, s in enumerate(sorted(students, key=lambda x: x["marks"], reverse=True)[:5], 1):
        print(f"{i}. {s['name']} - {s['marks']} marks ({grade(s['marks'])})")

def search_student():
    name = input("\nEnter student name: ").strip().lower()
    found = [s for s in students if name in s["name"].lower()]
    if not found:
        print("Student not found.")
        return
    for s in found:
        print(f"\nName: {s['name']}")
        print(f"Marks: {s['marks']}")
        print(f"Attendance: {s['attendance']}%")
        print(f"Grade: {grade(s['marks'])}")

def low_attendance():
    print("\n--- LOW ATTENDANCE (<75%) ---")
    found = False
    for s in students:
        if s["attendance"] < 75:
            print(f"{s['name']} - {s['attendance']}%")
            found = True
    if not found:
        print("No student below 75%.")

def add_student():
    try:
        name = input("Student name: ").strip()
        marks = float(input("Marks (0-100): "))
        attendance = float(input("Attendance % (0-100): "))
        if not name or not (0 <= marks <= 100) or not (0 <= attendance <= 100):
            print("Invalid input.")
            return
        students.append({"name": name, "marks": marks, "attendance": attendance})
        print("Student added successfully.")
    except ValueError:
        print("Please enter valid numbers.")

while True:
    print("\n==============================")
    print(" STUDENT PERFORMANCE ANALYTICS")
    print("==============================")
    print("1. Dashboard")
    print("2. Show all students")
    print("3. Top 5 students")
    print("4. Search student")
    print("5. Low attendance")
    print("6. Add student")
    print("7. Exit")

    choice = input("Choose option: ").strip()

    if choice == "1": dashboard()
    elif choice == "2": show_all()
    elif choice == "3": top_students()
    elif choice == "4": search_student()
    elif choice == "5": low_attendance()
    elif choice == "6": add_student()
    elif choice == "7":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")===
