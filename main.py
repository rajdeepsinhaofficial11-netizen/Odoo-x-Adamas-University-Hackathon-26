# ==============================
# HRMS - Single File (Programiz)
# ==============================

users = []
employees = []

# ------------------------------
# Helper: Find Employee by ID
# ------------------------------
def find_employee(emp_id):
    for emp in employees:
        if emp["id"] == emp_id:
            return emp
    return None

# ------------------------------
# Sign Up
# ------------------------------
def signup():
    print("\n===== SIGN UP =====")

    employee_id = input("Employee ID: ").strip()
    name = input("Name: ").strip()
    email = input("Email: ").strip()
    password = input("Password: ").strip()
    role = input("Role (Admin/Employee): ").strip().capitalize()

    if role not in ["Admin", "Employee"]:
        print("Invalid role! Enter only Admin or Employee.")
        return

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

    email = input("Email: ").strip()
    password = input("Password: ").strip()

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

    emp_id = input("Employee ID: ").strip()

    if find_employee(emp_id):
        print("Employee ID already exists!")
        return

    name = input("Name: ").strip()
    department = input("Department: ").strip()
    designation = input("Designation: ").strip()
    phone = input("Phone: ").strip()
    address = input("Address: ").strip()
    salary = input("Salary: ").strip()

    employees.append({
        "id": emp_id,
        "name": name,
        "department": department,
        "designation": designation,
        "phone": phone,
        "address": address,
        "salary": salary,
        "attendance": [],
        "leave_requests": []
    })

    print("Employee Added Successfully!")

# ------------------------------
# View Employees
# ------------------------------
def view_employees():
    if len(employees) == 0:
        print("\nNo Employees Found!")
        return

    print("\n===== EMPLOYEE LIST =====")
    for emp in employees:
        print("----------------------")
        print("ID:", emp["id"])
        print("Name:", emp["name"])
        print("Department:", emp["department"])
        print("Designation:", emp["designation"])
        print("Phone:", emp["phone"])
        print("Address:", emp["address"])
        print("Salary:", emp["salary"])

# ------------------------------
# Search Employee
# ------------------------------
def search_employee():
    print("\n===== SEARCH EMPLOYEE =====")
    emp_id = input("Enter Employee ID: ").strip()

    emp = find_employee(emp_id)
    if emp:
        print("\nEmployee Found")
        print("----------------------")
        print("ID:", emp["id"])
        print("Name:", emp["name"])
        print("Department:", emp["department"])
        print("Designation:", emp["designation"])
        print("Phone:", emp["phone"])
        print("Address:", emp["address"])
        print("Salary:", emp["salary"])
    else:
        print("Employee Not Found!")

# ------------------------------
# Update Employee
# ------------------------------
def update_employee():
    print("\n===== UPDATE EMPLOYEE =====")
    emp_id = input("Enter Employee ID: ").strip()

    emp = find_employee(emp_id)
    if emp:
        emp["name"] = input("New Name: ").strip()
        emp["department"] = input("New Department: ").strip()
        emp["designation"] = input("New Designation: ").strip()
        emp["phone"] = input("New Phone: ").strip()
        emp["address"] = input("New Address: ").strip()
        emp["salary"] = input("New Salary: ").strip()

        print("Employee Updated Successfully!")
    else:
        print("Employee Not Found!")

# ------------------------------
# Delete Employee
# ------------------------------
def delete_employee():
    print("\n===== DELETE EMPLOYEE =====")
    emp_id = input("Enter Employee ID: ").strip()

    emp = find_employee(emp_id)
    if emp:
        employees.remove(emp)
        print("Employee Deleted Successfully!")
    else:
        print("Employee Not Found!")

# ------------------------------
# View My Profile
# ------------------------------
def view_my_profile(user):
    emp = find_employee(user["employee_id"])

    if not emp:
        print("\nYour employee profile was not found.")
        print("Ask Admin to add your employee record first.")
        return

    print("\n===== MY PROFILE =====")
    print("ID:", emp["id"])
    print("Name:", emp["name"])
    print("Department:", emp["department"])
    print("Designation:", emp["designation"])
    print("Phone:", emp["phone"])
    print("Address:", emp["address"])
    print("Salary:", emp["salary"])

# ------------------------------
# Mark Attendance
# ------------------------------
def mark_attendance(user):
    emp = find_employee(user["employee_id"])

    if not emp:
        print("\nYour employee profile was not found.")
        print("Ask Admin to add your employee record first.")
        return

    status = input("Enter Attendance Status (Present/Absent/Half-day/Leave): ").strip()

    if status not in ["Present", "Absent", "Half-day", "Leave"]:
        print("Invalid attendance status!")
        return

    emp["attendance"].append(status)
    print("Attendance marked successfully!")

# ------------------------------
# View My Attendance
# ------------------------------
def view_my_attendance(user):
    emp = find_employee(user["employee_id"])

    if not emp:
        print("\nYour employee profile was not found.")
        return

    print("\n===== MY ATTENDANCE =====")
    if len(emp["attendance"]) == 0:
        print("No attendance records found.")
        return

    for i, record in enumerate(emp["attendance"], start=1):
        print(f"{i}. {record}")

# ------------------------------
# Apply Leave
# ------------------------------
def apply_leave(user):
    emp = find_employee(user["employee_id"])

    if not emp:
        print("\nYour employee profile was not found.")
        print("Ask Admin to add your employee record first.")
        return

    print("\n===== APPLY LEAVE =====")
    leave_type = input("Leave Type (Paid/Sick/Unpaid): ").strip()
    reason = input("Reason for Leave: ").strip()

    if leave_type not in ["Paid", "Sick", "Unpaid"]:
        print("Invalid leave type!")
        return

    leave_data = {
        "leave_type": leave_type,
        "reason": reason,
        "status": "Pending"
    }

    emp["leave_requests"].append(leave_data)
    print("Leave request submitted successfully!")

# ------------------------------
# View My Leave Requests
# ------------------------------
def view_my_leave_requests(user):
    emp = find_employee(user["employee_id"])

    if not emp:
        print("\nYour employee profile was not found.")
        return

    print("\n===== MY LEAVE REQUESTS =====")
    if len(emp["leave_requests"]) == 0:
        print("No leave requests found.")
        return

    for i, leave in enumerate(emp["leave_requests"], start=1):
        print(f"\nRequest {i}")
        print("Leave Type:", leave["leave_type"])
        print("Reason:", leave["reason"])
        print("Status:", leave["status"])

# ------------------------------
# View My Salary
# ------------------------------
def view_my_salary(user):
    emp = find_employee(user["employee_id"])

    if not emp:
        print("\nYour employee profile was not found.")
        return

    print("\n===== MY SALARY =====")
    print("Salary:", emp["salary"])

# ------------------------------
# View All Leave Requests (Admin)
# ------------------------------
def view_all_leave_requests():
    print("\n===== ALL LEAVE REQUESTS =====")

    found = False
    for emp in employees:
        if len(emp["leave_requests"]) > 0:
            found = True
            print(f"\nEmployee: {emp['name']} (ID: {emp['id']})")
            for i, leave in enumerate(emp["leave_requests"], start=1):
                print(f"  Request {i}")
                print(f"    Leave Type: {leave['leave_type']}")
                print(f"    Reason: {leave['reason']}")
                print(f"    Status: {leave['status']}")

    if not found:
        print("No leave requests found.")

# ------------------------------
# Approve Leave
# ------------------------------
def approve_leave():
    print("\n===== APPROVE LEAVE =====")
    emp_id = input("Enter Employee ID: ").strip()

    emp = find_employee(emp_id)
    if not emp:
        print("Employee Not Found!")
        return

    if len(emp["leave_requests"]) == 0:
        print("No leave requests found for this employee.")
        return

    print("\nLeave Requests:")
    for i, leave in enumerate(emp["leave_requests"], start=1):
        print(f"{i}. {leave['leave_type']} | {leave['reason']} | {leave['status']}")

    try:
        request_no = int(input("Enter request number to approve: "))
        if 1 <= request_no <= len(emp["leave_requests"]):
            emp["leave_requests"][request_no - 1]["status"] = "Approved"
            print("Leave approved successfully!")
        else:
            print("Invalid request number!")
    except:
        print("Please enter a valid number!")

# ------------------------------
# Reject Leave
# ------------------------------
def reject_leave():
    print("\n===== REJECT LEAVE =====")
    emp_id = input("Enter Employee ID: ").strip()

    emp = find_employee(emp_id)
    if not emp:
        print("Employee Not Found!")
        return

    if len(emp["leave_requests"]) == 0:
        print("No leave requests found for this employee.")
        return

    print("\nLeave Requests:")
    for i, leave in enumerate(emp["leave_requests"], start=1):
        print(f"{i}. {leave['leave_type']} | {leave['reason']} | {leave['status']}")

    try:
        request_no = int(input("Enter request number to reject: "))
        if 1 <= request_no <= len(emp["leave_requests"]):
            emp["leave_requests"][request_no - 1]["status"] = "Rejected"
            print("Leave rejected successfully!")
        else:
            print("Invalid request number!")
    except:
        print("Please enter a valid number!")

# ------------------------------
# Update Salary
# ------------------------------
def update_salary():
    print("\n===== UPDATE SALARY =====")
    emp_id = input("Enter Employee ID: ").strip()

    emp = find_employee(emp_id)
    if emp:
        new_salary = input("Enter New Salary: ").strip()
        emp["salary"] = new_salary
        print("Salary updated successfully!")
    else:
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
6. View All Leave Requests
7. Approve Leave
8. Reject Leave
9. Update Salary
10. Logout

============================
""")

        choice = input("Enter Choice: ").strip()

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
            view_all_leave_requests()
        elif choice == "7":
            approve_leave()
        elif choice == "8":
            reject_leave()
        elif choice == "9":
            update_salary()
        elif choice == "10":
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

1. View My Profile
2. Mark Attendance
3. View My Attendance
4. Apply Leave
5. View My Leave Requests
6. View My Salary
7. Logout

===========================
""")

        choice = input("Enter Choice: ").strip()

        if choice == "1":
            view_my_profile(user)
        elif choice == "2":
            mark_attendance(user)
        elif choice == "3":
            view_my_attendance(user)
        elif choice == "4":
            apply_leave(user)
        elif choice == "5":
            view_my_leave_requests(user)
        elif choice == "6":
            view_my_salary(user)
        elif choice == "7":
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

    choice = input("Enter Choice: ").strip()

    if choice == "1":
        signup()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Thank You!")
        break
    else:
        print("Invalid Choice!")
