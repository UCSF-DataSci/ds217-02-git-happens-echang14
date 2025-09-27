def load_students(filename):
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
        students.append((name, age, subject, grade))
    return students
    

