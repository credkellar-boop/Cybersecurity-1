#!/bin/bash

# Create all directories
mkdir -p 00_Foundation/Security_Plus
mkdir -p 01_CISO_Track/01_CISSP 01_CISO_Track/02_CISA_CRISC
mkdir -p 02_Pentester_Track/01_PenTest_Plus_CEH 02_Pentester_Track/02_OSCP
mkdir -p 03_SOC_Analyst_Track/01_CySA_Plus 03_SOC_Analyst_Track/02_GCIH
mkdir -p 04_Cloud_Security_Track/01_AWS_Azure_Security 04_Cloud_Security_Track/02_CCSP
mkdir -p Testing_and_Exams/Foundation_Tests Testing_and_Exams/Track_Specific_Quizzes Testing_and_Exams/Final_Simulated_Exams
mkdir -p Certification/templates

# Create baseline files
touch README.md CONTRIBUTING.md
touch Certification/cert_generator.py

# Populate subdirectories with standard README stubs
for dir in 00_Foundation/Security_Plus 01_CISO_Track/01_CISSP 01_CISO_Track/02_CISA_CRISC 02_Pentester_Track/01_PenTest_Plus_CEH 02_Pentester_Track/02_OSCP 03_SOC_Analyst_Track/01_CySA_Plus 03_SOC_Analyst_Track/02_GCIH 04_Cloud_Security_Track/01_AWS_Azure_Security 04_Cloud_Security_Track/02_CCSP Testing_and_Exams/Foundation_Tests Testing_and_Exams/Track_Specific_Quizzes Testing_and_Exams/Final_Simulated_Exams; do
    echo "# $(basename $dir) Module" > "$dir/README.md"
done

echo "✅ Cybersecurity-1 repository structure created successfully!"
