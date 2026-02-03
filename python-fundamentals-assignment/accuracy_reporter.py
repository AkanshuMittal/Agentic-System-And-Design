def accuracy_reporter(accuracy_value):
    return accuracy_value

try:
    accuracy_value = float(input("Enter the floating-point accuracy value: "))
    result = accuracy_reporter(accuracy_value)
    print(f"Model accuracy is {result}")

except ValueError:
    print("Invalid input. Please enter a numeric value.")

