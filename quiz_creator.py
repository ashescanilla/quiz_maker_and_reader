import os
import time
from colorama import init, Fore, Style
import sys

# Initialize Colorama
init(autoreset=True)

# Optional: clear terminal for better UI
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Function for animated text output
def animated_text(text, color=Fore.WHITE, delay=0.05):
    for char in text:
        print(color + char, end='', flush=True)
        time.sleep(delay)
    print()

# Function to save question to file
def save_question_to_file(file_name, question_data):
    with open(file_name, 'a') as file:
        file.write(f"QUESTION: {question_data['question']}\n")
        file.write(f"A. {question_data['a']}\n")
        file.write(f"B. {question_data['b']}\n")
        file.write(f"C. {question_data['c']}\n")
        file.write(f"D. {question_data['d']}\n")
        file.write(f"ANSWER: {question_data['answer'].upper()}\n")
        file.write("---\n")

# Function to view all questions
def view_all_questions(file_name):
    if not os.path.exists(file_name):
        print(Fore.RED + "No questions found! Please add questions first.")
        return
    with open(file_name, 'r') as file:
        print(Fore.GREEN + file.read())

# Function to remove a question (basic version that just removes the last question)
def remove_last_question(file_name):
    if not os.path.exists(file_name):
        print(Fore.RED + "No questions to remove!")
        return
    with open(file_name, 'r') as file:
        lines = file.readlines()
    if len(lines) < 7:
        print(Fore.RED + "❌ Not enough data to remove a question.")
        return
    with open(file_name, 'w') as file:
        file.writelines(lines[:-7])
    print(Fore.GREEN + "✅ Last question removed successfully!")