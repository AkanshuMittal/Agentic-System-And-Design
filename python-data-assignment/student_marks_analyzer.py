def student_marks_analyzer(marks):
    full_list = marks[0:]
    first_3_marks = marks[0:3]
    last_3_marks = marks[-3:]
    
    return full_list, first_3_marks, last_3_marks

def highest_mark(marks):
    highest = max(marks)
    
    return highest

def lowest_mark(marks):
    lowest = min(marks)
    
    return lowest

def average_mark(marks):
    total = sum(marks)
    average = total/len(marks)
    
    return average

def main():
    marks = [34, 23, 45, 56, 67,76, 89, 12, 99]
    
    full_list, first_3_marks, last_3_marks = student_marks_analyzer(marks)
    highest = highest_mark(marks)
    lowest = lowest_mark(marks)
    average = average_mark(marks)
    
    print(f"First 3 marks: {first_3_marks}")
    print(f"Last 3 marks: {last_3_marks}")
    print(f"Highest: {highest}")
    print(f"Lowest: {lowest}")
    print(f"Average: {average}")
    
        
main()