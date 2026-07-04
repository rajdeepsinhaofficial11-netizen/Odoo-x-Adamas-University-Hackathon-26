# ==============================
# HRMS - Single File (Programiz)
# ==============================

users = []
employees = []

# ------------------------------
# Sign Up
# ------------------------------
def signup():
    print("\n===== SIGN UP =====")

    employee_id = input("Employee ID: ")
    name = input("Name: ")
    email = input("Email: ")
    password = input("Password: ")
    role = input("Role (Admin/Employee): ").capitalize()

    for user in users:
        if user["email"] == email:
            print("Email already registered!")
            return

    users.append({
        "employee_id": employee_id,
        "name": name,
        "email": email,
        "password": password,
        "role": role
    })

    print("Signup Successful!")

# ------------------------------
# Login
# ------------------------------
def login():
    print("\n===== LOGIN =====")

    email = input("Email: ")
    password = input("Password: ")

    for user in users:
        if user["email"] == email and user["password"] == password:
            print(f"\nWelcome {user['name']} ({user['role']})")

            if user["role"] == "Admin":
                admin_menu()
            else:
                employee_menu(user)

            return

    print("Invalid Email or Password!")

# ------------------------------
# Add Employee
# ------------------------------
def add_employee():
    print("\n===== ADD EMPLOYEE =====")

    emp_id = input("Employee ID: ")
    name = input("Name: ")
    department = input("Department: ")
    salary = input("Salary: ")

    employees.append({
        "id": emp_id,
        "name": name,
        "department": department,
        "salary": salary
    })

    print("Employee Added Successfully!")

# ------------------------------
# View Employees
# ------------------------------
def view_employees():

    if len(employees) == 0:
        print("No Employees Found!")
        return

    print("\n===== EMPLOYEE LIST =====")

    for emp in employees:
        print("----------------------")
        print("ID:", emp["id"])
        print("Name:", emp["name"])
        print("Department:", emp["department"])
        print("Salary:", emp["salary"])

# ------------------------------
# Search Employee
# ------------------------------
def search_employee():

    emp_id = input("Enter Employee ID: ")

    for emp in employees:
        if emp["id"] == emp_id:
            print("\nEmployee Found")
            print(emp)
            return

    print("Employee Not Found!")

# ------------------------------
# Delete Employee
# ------------------------------
def delete_employee():

    emp_id = input("Enter Employee ID: ")

    for emp in employees:
        if emp["id"] == emp_id:
            employees.remove(emp)
            print("Employee Deleted Successfully!")
            return

    print("Employee Not Found!")

# ------------------------------
# Update Employee
# ------------------------------
def update_employee():

    emp_id = input("Enter Employee ID: ")

    for emp in employees:
        if emp["id"] == emp_id:

            emp["name"] = input("New Name: ")
            emp["department"] = input("New Department: ")
            emp["salary"] = input("New Salary: ")

            print("Employee Updated Successfully!")
            return

    print("Employee Not Found!")

# ------------------------------
# Admin Menu
# ------------------------------
def admin_menu():

    while True:

        print("""
======== ADMIN MENU ========

1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Logout

============================
""")

        choice = input("Enter Choice: ")

        if choice == "1":
            add_employee()

        elif choice == "2":
            view_employees()

        elif choice == "3":
            search_employee()

        elif choice == "4":
            update_employee()

        elif choice == "5":
            delete_employee()

        elif choice == "6":
            break

        else:
            print("Invalid Choice!")

# ------------------------------
# Employee Menu
# ------------------------------
def employee_menu(user):

    while True:

        print("""
====== EMPLOYEE MENU ======

1. View Employees
2. Logout

===========================
""")

        choice = input("Enter Choice: ")

        if choice == "1":
            view_employees()

        elif choice == "2":
            break

        else:
            print("Invalid Choice!")

# ------------------------------
# Main Menu
# ------------------------------
while True:

    print("""
=========================
 HRMS MANAGEMENT SYSTEM
=========================

1. Sign Up
2. Login
3. Exit

=========================
""")

    choice = input("Enter Choice: ")

    if choice == "1":
        signup()

    elif choice == "2":
        login()

    elif choice == "3":
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
