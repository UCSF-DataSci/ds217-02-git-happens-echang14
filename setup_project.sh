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
EOF
echo "Data analysis script placeholder"

cat > src/data_analysis_functions.py << 'EOF'
EOF
echo "Data analysis functions script placeholder"


chmod +x setup_project.sh