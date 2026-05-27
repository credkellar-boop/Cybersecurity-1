import os

# Define the directory structure
folders = [
    "00_Foundation/Security_Plus",
    "01_CISO_Track/01_CISSP",
    "01_CISO_Track/02_CISA_CRISC",
    "02_Pentester_Track/01_PenTest_Plus_CEH",
    "02_Pentester_Track/02_OSCP",
    "03_SOC_Analyst_Track/01_CySA_Plus",
    "03_SOC_Analyst_Track/02_GCIH",
    "04_Cloud_Security_Track/01_AWS_Azure_Security",
    "04_Cloud_Security_Track/02_CCSP",
    "Testing_and_Exams/Foundation_Tests",
    "Testing_and_Exams/Track_Specific_Quizzes",
    "Testing_and_Exams/Final_Simulated_Exams",
    "Certification/templates"
]

files = [
    "README.md",
    "CONTRIBUTING.md",
    "Certification/cert_generator.py"
]

# Create folders
for folder in folders:
    os.makedirs(folder, exist_ok=True)
    # Create a stub README inside each subfolder
    readme_path = os.path.join(folder, "README.md")
    if not os.path.exists(readme_path):
        with open(readme_path, "w") as f:
            f.write(f"# {os.path.basename(folder)} Module\n\nContent coming soon.")

# Create top-level files
for file in files:
    if not os.path.exists(file):
        with open(file, "w") as f:
            if "cert_generator.py" in file:
                f.write("#!/usr/bin/env python3\nprint('Certificate Generator Initialized')\n")
            else:
                f.write(f"# {file.split('.')[0]}\n")

print("✅ Cybersecurity-1 repository structure created successfully!")
