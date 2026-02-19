def average(scores):
    
    average = sum(scores)/len(scores)
        
    return average

def has_admin_access(roles):
    if "admin" in roles:
        return True
    else:
        return False
    
def main():
    users = [
    {
        "name": "Abhay",
        "scores": [43, 56, 12, 67],
        "roles": {"editor", "viewer"}
    },
    {
        "name": "Mukul",
        "scores": [13, 96, 42, 47],
        "roles": {"admin", "editor", "viewer"}
    }
]
    for user in users:
        user_name = user["name"]
        average_score = average(user["scores"])
        admin_access = has_admin_access(user["roles"])
        
        print(f"User Name: {user_name}")
        print(f"Average Score: {average_score}")
        print(f"Admin Access: {'Yes' if admin_access else 'No'}")
        print()  
   
    
main()