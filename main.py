import time
from datetime import datetime

def start_session():
    task = input("Please input the name of the task: ")
    print("\nThe study session has begun... Keep your concentration! ")
    
    start_time = time.time()
    distractions = 0

    while True:
        print("\nOptions:")
        print("1. Log distraction")
        print("2. End session")
        
        choice = input("Enter choice: ")

        if choice == "1":
            distractions += 1
            print("Distraction noted! ⚠️ Stay focused!")

        elif choice == "2":
            end_time = time.time()
            duration = end_time - start_time
            minutes = round(duration / 60, 2)

            print("\n📊 Session Summary")
            print(f"Task: {task}")
            print(f"Time Studied: {minutes} minutes")
            print(f"Distractions: {distractions}")

            save_session(task, minutes, distractions)
            break

        else:
            print("Invalid choice!")
