def total_salary(path):
    total = 0
    count = 0
    
    try:
        with open(path, 'r', encoding='utf-8') as file:
            for line in file:
                data = line.strip().split(',')
                if len(data) == 2:
                    name, salary = data
                    total += int(salary)
                    count += 1
                    
        if count == 0:
            return 0, 0
            
        average = total / count
        return total, int(average) 

    except FileNotFoundError:
        print("pass")
        return 0, 0
    except Exception as e:
        print(f"error{e}")
        return 0, 0

# total, average = total_salary("salary_file.txt")
