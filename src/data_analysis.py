
def load_students(filename):
    """To Do: read student data from a CSV file and return a list student data"""
    with open(filename, "r") as file:
        lines = file.readlines()
    
    students = []
    for line in lines[1:]:  # skip header
        fields = line.strip().split(",")
        name = fields[0]
        age = int(fields[1])
        grade = int(fields[2])
        subject = fields[3]
        students.append((name, age, grade, subject))
    return students
    

    
def calculate_average_grade(students):
    """Calculate average grade"""
    if not students:
        return 0
    total_grade = sum(s[2] for s in students)
    return total_grade / len(students)

def count_math_students(students):
    """Count students in math"""
    return sum(1 for s in students if s[3] == "Math")
    

def generate_report(total, average_grade, math_count):
    """Create formatted report string."""
    report = (
        f"Student Analysis Report\n"
        f"-----------------------\n"
        f"Total students: {total}\n"
        f"Average grade: {average_grade:.1f}\n"
        f"Math students: {math_count}\n"
    )
    return report

def save_report(report, filename):
    """Save report to a file""" 
    with open(filename, "w") as f:
        f.write(report)

def main():
    """Main function to generate and save report"""
    students = load_students("students.csv")
    total_students = len(students)
    average_grade = calculate_average_grade(students)
    math_students = count_math_students(students)
    report = generate_report(total_students, average_grade, math_students)
    save_report(report, "report.txt")

if __name__ == "__main__": 
    main()