import time
import random
from datetime import datetime
from colorama import Fore, init
import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression

def train_model():
    try:
        data = pd.read_csv("data.txt", names=["date", "task", "minutes", "distractions"])

        if len(data) < 5:
            return None, None

        X = data[["minutes", "distractions"]]

        y_reg = data["minutes"] / (data["distractions"] + 1)
        y_class = y_reg.apply(lambda x: 1 if x > 20 else 0)

        reg_model = LinearRegression()
        reg_model.fit(X, y_reg)

        clf_model = LogisticRegression()
        clf_model.fit(X, y_class)

        return reg_model, clf_model

    except:
        return None, None


def predict_results(reg_model, clf_model, minutes, distractions):
    if reg_model is None or clf_model is None:
        return "Not enough data", "Not enough data"

    score = reg_model.predict([[minutes, distractions]])[0]
    label = clf_model.predict([[minutes, distractions]])[0]

    label_text = "High Productivity 🚀" if label == 1 else "Low Productivity ⚠️"

    return round(score, 2), label_text
init(autoreset=True)

# ---------------- QUOTES ----------------
quotes = [
    "Stay focused, you're doing great!",
    "Small progress is still progress.",
    "Discipline beats motivation.",
    "Push yourself, no one else will.",
    "Success starts with consistency."
]

def show_quote():
    print(Fore.CYAN + "\n💡 " + random.choice(quotes) + "\n")

# ---------------- STUDY SESSION ----------------
def start_session():
    task = input(Fore.YELLOW + "Enter task name: ")

    print(Fore.GREEN + "\nStudy session started... Stay focused! 💪")
    show_quote()

    start_time = time.time()
    distractions = 0

    while True:
        print(Fore.BLUE + "\nOptions:")
        print("1. Log distraction")
        print("2. End session")

        choice = input("Enter choice: ")

        if choice == "1":
            distractions += 1
            print(Fore.RED + "⚠️ Distraction noted!")

        elif choice == "2":
            end_time = time.time()
            duration = end_time - start_time
            minutes = round(duration / 60, 2)

            print(Fore.MAGENTA + "\n📊 Session Summary")
            print(f"Task: {task}")
            print(f"Time Studied: {minutes} minutes")
            print(f"Distractions: {distractions}")

            # ML Prediction

            reg_model, clf_model = train_model()
            score, label = predict_results(reg_model, clf_model, minutes, distractions)

            print(Fore.CYAN + f"🤖 Productivity Score: {score}")
            print(Fore.YELLOW + f"📌 Session Type: {label}")

            save_session(task, minutes, distractions)
            break

        else:
            print(Fore.RED + "Invalid choice!")

# ---------------- POMODORO ----------------
def pomodoro():
    print(Fore.GREEN + "\n🍅 Pomodoro started: 25 minutes focus!")
    show_quote()

    time.sleep(1500)

    print(Fore.YELLOW + "\n⏸️ Take a 5-minute break!")
    time.sleep(300)

    print(Fore.GREEN + "\n✅ Pomodoro complete!")

# ---------------- SAVE DATA ----------------
def save_session(task, minutes, distractions):
    date = datetime.now().strftime("%Y-%m-%d")

    with open("data.txt", "a") as file:
        file.write(f"{date},{task},{minutes},{distractions}\n")

    print(Fore.GREEN + "Session saved ✅")

# ---------------- VIEW SUMMARY ----------------
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
        print(Fore.RED + "No study sessions found.")

# ---------------- MAIN ----------------
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
            print(Fore.GREEN + "Goodbye! Stay productive 🚀")
            break
        else:
            print(Fore.RED + "Invalid choice!")

if __name__ == "__main__":
    main()

