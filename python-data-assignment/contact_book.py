def contact_book(contacts, name):
    print("All Contacts: ")
    for key,value in contacts.items():
        print(f"{key}:{value}")
    print()
        
    if name in contacts:
        print("Phone number: ", contacts[name])
    else:
        print("Contact not found")
        

contacts = {
    "Ravi": "9876543210",
    "Anita": "9123456780",
    "Abhay": "9845230924"
}

name = input("Enter the name: ")

contact_book(contacts, name)