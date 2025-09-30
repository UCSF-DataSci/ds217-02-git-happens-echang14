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
            "math_students": 0
        }
    
    total_students = len(students)
    highest_grade = max(s[2] for s in students)
    lowest_grade = min(s[2] for s in students)
    average_grade = sum(s[2] for s in students) / total_students
    math_students = sum(1 for s in students if s[3] == "Math")
    science_students = sum(1 for s in students if s[3] == "Science") 
    english_students = sum(1 for s in students if s[3] == "English") 
    return {"total_students:", total_students,
            "average_grade:", average_grade,
            "math_students:", math_students,
            "highest_grade:", highest_grade,
            "lowest_grade:", lowest_grade,
            "science_students:", science_students,
            "english_students:", english_students
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
    with open(filename, "w") as f:
        f.write("STUDENT DATA ANALYSIS REPORT\n")
        f.write("============================\n\n")
        f.write(f"Total Students: {results['total_students']}\n")
        f.write(f"Average Grade: {results['average_grade']:.1f}\n")
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
