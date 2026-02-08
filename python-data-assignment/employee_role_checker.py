def employee_details(employee):
    print("Employee ID:", employee[0])
    print("Employee Name:", employee[1])
    print("Department:", employee[2])
    print()


def role_checker(roles):
    if "admin" in roles:
        print(f"Admin Access: Yes")
    else: 
        print(f"Admin Access: No")
        
def main():
    employee = (1, "Abhay", "CSE")
    roles = {"admin", "editor", "viewer"}
    
    employee_details(employee)
    role_checker(roles)
    
main()
