def read_numbers_from_file(filename):
    numbers = []
    
    with open(filename, "r") as file:
        print("File opened successfully")
        
        for line in file:
            cleaned_line = line.strip()
            
            if cleaned_line:
                number = int(cleaned_line)
                numbers.append(number)
    print(f"Read {len(numbers)} numbers")
    
    return numbers 


def statistics(numbers):
    total_count  = len(numbers)
    total_sum = sum(numbers)
    average = total_sum / total_count if total_count > 0 else 0
    
    print("Computation completed")
    
    return total_count, total_sum, average


def write_log(filename, count, total_sum, average):
    with open(filename, "w") as log_file:
        log_file.write("File opened successfully\n")
        log_file.write(f"Read {count} numbers\n")
        log_file.write(f"Sum: {total_sum}\n")
        log_file.write(f"Average: {average}\n")
        log_file.write("Processing completed\n")
        
def main():
    input_file = "python-files-assignment/numbers.txt"
    log_file = "python-files-assignment/results.log"
    
    numbers = read_numbers_from_file(input_file)

    count, total_sum, average = statistics(numbers)

    write_log(log_file, count, total_sum, average)
    

main()


    
    