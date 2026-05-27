#!/usr/bin/env python3
import sys
import time

def run_quiz():
    questions = [
        {
            "question": "Which component of the CIA Triad is compromised if an attacker executes a successful DoS (Denial of Service) attack against a web server?",
            "options": ["A. Confidentiality", "B. Integrity", "C. Availability", "D. Accountability"],
            "answer": "C"
        },
        {
            "question": "A security engineer configures a system where users are authenticated via a password, a hardware token, and a fingerprint scan. How many factors of authentication are being used?",
            "options": ["A. One", "B. Two", "C. Three", "D. Four"],
            "answer": "C"
        },
        {
            "question": "Which of the following cloud service models places the highest amount of security management responsibility strictly on the customer?",
            "options": ["A. SaaS", "B. PaaS", "C. IaaS", "D. XaaS"],
            "answer": "C"
        },
        {
            "question": "An employee receives an urgent email appearing to come from the CEO, demanding wire transfers to a vendor immediately. What type of social engineering attack is this?",
            "options": ["A. Vishing", "B. Whaling", "C. Tailgating", "D. Smishing"],
            "answer": "B"
        },
        {
            "question": "What calculation is used to determine the Expected Annual Loss based on the Single Loss Expectancy (SLE) and Annual Rate of Occurrence (ARO)?",
            "options": ["A. ALE = SLE * ARO", "B. ALE = SLE / ARO", "C. ALE = SLE + ARO", "D. ALE = SLE - ARO"],
            "answer": "A"
        }
    ]

    print("==================================================")
    print("🛡️  CYBERSECURITY-1: SECURITY+ BASELINE QUIZ  🛡️")
    print("==================================================")
    print("Pass mark required: 80% (4/5 Correct Answers)\n")
    time.sleep(1)

    score = 0
    
    for i, q in enumerate(questions, 1):
        print(f"Question {i}: {q['question']}")
        for option in q['options']:
            print(option)
            
        while True:
            choice = input("\nYour Answer (A, B, C, or D): ").strip().upper()
            if choice in ['A', 'B', 'C', 'D']:
                break
            print("❌ Invalid input. Please enter A, B, C, or D.")
            
        if choice == q['answer']:
            print("✨ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect. The correct answer was {q['answer']}.\n")
        time.sleep(0.5)

    final_percentage = (score / len(questions)) * 100
    print("==================================================")
    print(f"QUIZ COMPLETE! Your Score: {score}/{len(questions)} ({final_percentage}%)")
    print("==================================================")

    if final_percentage >= 80:
        print("🎉 Congratulations! You passed the Foundation Exam.")
        print("🔓 Phase 2 tracks are now unlocked for your role path!")
        sys.exit(0)
    else:
        print("💔 You did not meet the 80% passing score threshold.")
        print("📚 Review the 00_Foundation materials and try again!")
        sys.exit(1)

if __name__ == "__main__":
    try:
        run_quiz()
    except KeyboardInterrupt:
        print("\n\nQuiz aborted. Goodbye!")
