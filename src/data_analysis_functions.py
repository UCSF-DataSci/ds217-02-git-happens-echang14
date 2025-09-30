def load_data(filename):
    """Generic loader that checks file extension."""
    if filename.endswith(".csv"):
        return load_csv(filename)
    else:
        raise ValueError("Unsupported file format. Only CSV is supported.")
    
def load_csv(filename):
    """Read CSV"""
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
   

def analyze_data(students):
    """Return dictionary with multiple statistics"""
    if not students:
        return {
            "total_students": 0,
            "average_grade": 0,
            "highest_grade": 0,
            "lowest_grade": 0,
            "subjects": {}
        }
    
    total_students = len(students)
    highest_grade = max(s[2] for s in students)
    lowest_grade = min(s[2] for s in students)
    average_grade = sum(s[2] for s in students) / total_students
    
    # Count subjects into a dictionary
    subjects = {}
    for s in students:
        subj = s[3]
        subjects[subj] = subjects.get(subj, 0) + 1
    
    return {
        "total_students": total_students,
        "average_grade": average_grade,
        "highest_grade": highest_grade,
        "lowest_grade": lowest_grade,
        "subjects": subjects
    }


def analyze_grade_distribution(grades): 
    """Count grades by letter grade ranges"""
    distribution = {"A": 0, "B": 0, "C": 0, "D": 0, "F": 0 }
    
    for g in grades:
        if 90 <= g <= 100:
            distribution["A"] +=1
        elif 80 <= g <= 89:
            distribution["B"] +=1
        elif 70 <= g <= 79:
            distribution["C"] +=1
        elif 60 <= g <= 69:
            distribution["D"] +=1
        else:
            distribution["F"] +=1
    
    total = len(grades)
    percentages = {}
    for letter, count in distribution.items():
        percent = (count / total * 100) if total > 0 else 0
        percentages[letter] = {"count": count, "percent": f"{percent:.1f}%"}
    return percentages

def save_results(results, filename): 
    """Save detailed report"""
    with open(filename, "a") as f:
        f.write("      \n\n")
        f.write("Advanced Student Analysis Report\n")
        f.write("============================\n\n")
        f.write(f"Highest Grade: {results['highest_grade']}\n")
        f.write(f"Lowest Grade: {results['lowest_grade']}\n\n")

        f.write("Students by Subject:\n")
        for subject, count in results["subjects"].items():
            f.write(f"  {subject}: {count}\n")
        f.write("\n")

        f.write("Grade Distribution:\n")
        for letter, data in results["grade_distribution"].items():
            f.write(f"  {letter}: {data['count']} ({data['percent']})\n")        

def main(): 
    """Orchestrate the analysis using all functions"""
    students = load_data("data/students.csv")
    stats = analyze_data(students)
    grades = [s[2] for s in students]
    grade_distribution = analyze_grade_distribution(grades)
    stats["grade_distribution"] = grade_distribution
    save_results(stats, "output/analysis_report.txt")

if __name__ == "__main__":
    main()
