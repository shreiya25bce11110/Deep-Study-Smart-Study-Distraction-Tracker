import time
import random
from datetime import datetime
from colorama import Fore, Style, init

# to start or initialize colorama
init(autoreset=True)

#motivational qoutes to stay motivated
quotes = [
    "Stay focused, you're doing great!",
    "Small progress is still progress.",
    "Discipline beats motivation.",
    "Push yourself, no one else will.",
    "Success starts with consistency."
]

def show_quote():
    print(Fore.CYAN + " \n ✨" + random.choice(quotes) + "\n")

def start_session():
    task = input("Please input the name of the task: ")
    print("\nThe study session has begun... Keep your concentration! ")
    
    start_time = time.time()
    distractions = 0

    while True:
        print(Fore.BLUE + "\nOptions:")
        print("1. Log distraction")
        print("2. End session")
        
        choice = input("Enter your choice from the above options: ")

        if choice == "1":
            distractions += 1
            print(Fore.RED + "Distraction noted! ⚠️ Stay focused!")

        elif choice == "2":
            end_time = time.time()
            duration = end_time - start_time
            minutes = round(duration / 60, 2)

            print(Fore.MAGENTA + "\n Session Summary")
            print(f"Task: {task}")
            print(f"Time Studied: {minutes} minutes")
            print(f"Distractions: {distractions}")

            save_session(task, minutes, distractions)
            break

        else:
            print(Fore.RED + "Invalid choice!")
def pomodoro():
    print(Fore.GREEN + "\n🍅 Pomodoro started: 25 minutes focus!")
    show_quote()
   
    time.sleep(1500) # 25 minutes
   
    print(Fore.YELLOW + "\n⏸️ Time for a 5-minute break!")
    time.sleep(300)

    print(Fore.GREEN + "\n✅ Pomodoro session complete!")
            
def save_session(task, minutes, distractions):
    date = datetime.now().strftime("%Y-%m-%d")

    with open("data.txt", "a") as file:
        file.write(f"{date},{task},{minutes},{distractions}\n")

    print(Fore.GREEN + "Session saved successfully ✅")
    
def view_summary():
    try:
        with open("data.txt", "r") as file:
            lines = file.readlines()

            if not lines:
                print(Fore.YELLOW + "No data available.")
                return

            print(Fore.CYAN + "\n📅 Study History:\n")
            total_time = 0
            
            for line in lines:
                date, task, minutes, distractions = line.strip().split(",")
                total_time += float(minutes)
                print(f"{date} | {task} | {minutes} mins | {distractions} distractions")
            
            print(Fore.GREEN + f"\n📈 Total Study Time: {round(total_time,2)} minutes")

    except FileNotFoundError:
        print("No study sessions found yet.")
        
def main():
    while True:
        print(Fore.CYAN + "\n==== FocusFlow ====")
        print("1. Start Study Session")
        print("2. Pomodoro Mode")
        print("3. View Summary")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            start_session()
        elif choice == "2":
            pomodoro()
        elif choice == "3":
            view_summary()
        elif choice == "4":
            print(Fore.GREEN + "Goodbye! Stay productive.")
            break
        else:
            print(Fore.RED + "Invalid choice!")

if __name__ == "__main__":
    main()

