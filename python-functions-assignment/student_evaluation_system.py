def greeting_message(name):
    return f"Hello, {name}"


def student_score(scores):
    subjects = len(scores)
    total = 0
    
    for i in scores:
        total += i
        
    average_score = (total)/(subjects)
    
    return subjects, average_score


def pass_fail(average_score):
    if average_score >= 50:
        return "Pass"
    else:
        return "Fail"
    
    
def main():
    name = input("Enter your name: ")  
    scores = [54, 67, 56, 23, 78]
    
    greeting = greeting_message(name)
    subjects, average_score = student_score(scores)
    result = pass_fail(average_score)
    
    print(greeting)
    print(f"Subjects: {subjects}")
    print(f"Average Score: {average_score}")
    print(f"Result: {result}")
    
    
main()
    




