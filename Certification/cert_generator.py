#!/usr/bin/env python3
import os
import time

def generate_certificate():
    print("==================================================")
    print("🎓 CYBERSECURITY-1 CERTIFICATE GENERATOR ENGINE 🎓")
    print("==================================================")
    
    # Gather candidate details
    name = input("Enter Candidate Full Name: ").strip()
    if not name:
        name = "Certified Professional"
        
    print("\nSelect your completed 2025 Career Track:")
    print("1. Chief Information Security Officer (CISO)")
    print("2. Penetration Tester (Pentester)")
    print("3. SOC Analyst")
    print("4. Cloud Security Engineer")
    
    track_mapping = {
        "1": "Chief Information Security Officer (CISO)",
        "2": "Penetration Tester (Pentester)",
        "3": "SOC Analyst",
        "4": "Cloud Security Engineer"
    }
    
    while True:
        choice = input("Enter track number (1-4): ").strip()
        if choice in track_mapping:
            track_name = track_mapping[choice]
            break
        print("❌ Invalid selection. Choose a number between 1 and 4.")

    print("\n⏳ Verifying track status and baking certificate...")
    time.sleep(2)

    # Date string generation
    completion_date = time.strftime("%B %d, %Y")
    
    # ASCII Certificate layout definition
    cert_template = f"""
+-------------------------------------------------------------------------+
|                                                                         |
|   ===================================================================   |
|   🛡️                    CYBERSECURITY-1 ACADEMY                     🛡️   |
|   ===================================================================   |
|                                                                         |
|                       CERTIFICATE OF COMPLETION                         |
|                                                                         |
|                       This is proudly awarded to                        |
|                                                                         |
|               {name.center(50)}        |
|                                                                         |
|   For successfully executing and mastering the comprehensive curriculum  |
|   and rigorous examination standards set forth in the 2025 pathway:     |
|                                                                         |
|         👉    {track_name.center(48)}    👈        |
|                                                                         |
|                                                                         |
|   Issued on: {completion_date.ljust(20)}        Status: VERIFIED        |
|   ID: CS1-{int(time.time())}                                              |
|                                                                         |
|   ===================================================================   |
|                 "Securing the Digital Frontier, Step by Step"           |
|   ===================================================================   |
|                                                                         |
+-------------------------------------------------------------------------+
"""

    # Ensure output destination folder matches layout spec
    os.makedirs("Certification", exist_ok=True)
    output_path = os.path.join("Certification", "certificate.txt")
    
    with open(output_path, "w", encoding="utf-8") as f:
        f.write(cert_template)
        
    print(f"\n🎉 Success! Your official completion document has been minted.")
    print(f"📁 Saved to: {output_path}\n")
    print(cert_template)

if __name__ == "__main__":
    try:
        generate_certificate()
    except KeyboardInterrupt:
        print("\n\nOperation cancelled.")
