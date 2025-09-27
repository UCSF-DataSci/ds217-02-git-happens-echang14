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
    """To Do: read student data from a CSV file and return a list student data"""
    

    
def calculate_average_grade(students):
    """Calculate average grade"""
    

def count_math_students(students):
    """Count students in math"""
    

def generate_report():
    """Load students, calculate stats, and return formatted report string."""
    

def save_report(report, filename):
    """Save report to a file""" 
    

def main():
    """Main function to generate and save report"""

EOF
echo "Data analysis script placeholder"

cat > src/data_analysis_functions.py << 'EOF'
def load_data(filename):
    """Generic loader that checks file extension."""
    
def load_csv(filename):
    """Read CSV"""
   

def analyze_data(students):
    """Return dictionary with multiple statistics"""

def analyze_grade_distribution(grades): 
    """Count grades by letter grade ranges"""

def save_results(results, filename): 
    """Save detailed report"""

def main(): 
    """Orchestrate the analysis using all functions"""
EOF
echo "Data analysis functions script placeholder"


chmod +x setup_project.sh