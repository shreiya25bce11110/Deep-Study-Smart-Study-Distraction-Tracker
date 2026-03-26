import time
import random
from datetime import datetime
from colorama import Fore, Style, init

# to start or initialize colorama
init(autoreset=True)



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
            
def save_session(task, minutes, distractions):
    date = datetime.now().strftime("%Y-%m-%d")

    with open("data.txt", "a") as file:
        file.write(f"{date},{task},{minutes},{distractions}\n")

    print("Session saved successfully ✅")
def view_summary():
    try:
        with open("data.txt", "r") as file:
            lines = file.readlines()

            if not lines:
                print("No data available.")
                return

            print("\n📅 Study History:\n")
            for line in lines:
                date, task, minutes, distractions = line.strip().split(",")
                print(f"{date} | {task} | {minutes} mins | {distractions} distractions")

    except FileNotFoundError:
        print("No study sessions found yet.")
def main():
    while True:
        print("\n==== FocusFlow ====")
        print("1. Start Study Session")
        print("2. View Summary")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            start_session()
        elif choice == "2":
            view_summary()
        elif choice == "3":
            print("Goodbye! Stay productive 🚀")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()

