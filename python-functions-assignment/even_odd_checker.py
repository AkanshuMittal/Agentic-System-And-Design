def even_odd_checker(number):
    if number%2==0:
        return "Even"
    
    else:
        return "Odd"
    

number = int(input("Enter the number: "))  
result = even_odd_checker(number)

print(f"Number is {result}")

    
    
