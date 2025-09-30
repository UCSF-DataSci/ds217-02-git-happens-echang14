#!/bin/bash

mkdir -p src data output
echo "Project directories created: src, data, output"

touch .gitignore
touch requirements.txt
echo "Created .gitignore and requirements.txt"

cat > data/students.csv << 'EOF'
name,age,grade,subject
Alice,20,85,Math
Bob,19,92,Science
Charlie,21,78,English
Diana,20,88,Math
Eve,22,95,Science
Frank,19,82,History
Grace,21,91,Math
Henry,20,76,Science
EOF

cat > src/data_analysis.py << 'EOF'
def load_students(filename):
    ""Read student data from a CSV file and return a list student data"""
    # TODO: Open file, read lines, skip header
    # TODO: Split each line by comma
    # TODO: Return list of student data
    pass

    
def calculate_average_grade(students):
    """Calculate average grade"""
    # TODO: Sum all grades
    # TODO: Divide by number of students
    pass
    

def count_math_students(students):
    """Count students in math"""
    # TODO: Count students where subject is Math
    pass
    

def generate_report():
    """Load students, calculate stats, and return formatted report string."""
    # TODO: Create formatted string with results
    # TODO: Use f-strings with .1f for decimals
    pass


def save_report(report, filename):
    """Save report to a file""" 
    # TODO: Create output directory if needed
    # TODO: Write report to file
    pass

    

def main():
    """Main function to generate and save report"""
    # TODO: Load data
    # TODO: Calculate statistics
    # TODO: Generate and save report
    pass
EOF
echo "Data analysis script placeholder"

cat > src/data_analysis_functions.py << 'EOF'
def load_data(filename):
    """Generic loader that checks file extension."""
    # TODO: Check file extension
    # TODO: Call appropriate loader
    pass
    
def load_csv(filename):
    """Read CSV"""
    # TODO: Same technique as basic script
    pass
   

def analyze_data(students):
    """Return dictionary with multiple statistics"""
    # TODO: Calculate multiple statistics
    # TODO: Return dictionary of results
    pass

def analyze_grade_distribution(grades): 
    """Count grades by letter grade ranges"""
    # TODO: Count A (90-100), B (80-89), etc.
    pass


def save_results(results, filename): 
    """Save detailed report"""
    # TODO: Format and write comprehensive report
    pass

def main(): 
    """Orchestrate the analysis using all functions"""
    # TODO: Orchestrate the analysis
    pass

EOF
echo "Data analysis functions script placeholder"


chmod +x setup_project.sh