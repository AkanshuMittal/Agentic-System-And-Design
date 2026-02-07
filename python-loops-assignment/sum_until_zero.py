def sum_until_zero():
    total_sum = 0
    
    while True:
        number = int(input("Enter the number: "))
        
        if number == 0:
            break
        
        total_sum += number
        
    print(f"Total: {total_sum}")
       
        
sum_until_zero()