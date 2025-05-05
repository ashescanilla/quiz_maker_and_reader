# Import necessary modules:
# -> tkinter (GUI)
import tkinter as tk
# -> messagebox (for errors)
from tkinter import messagebox
# -> random (for random question selection)
import random
# -> sys (for exiting the app)
import sys

# Function: Load Questions from Custom File
def load_questions_from_custom_file(file_path):
# -> Initialize empty question list
    list_of_questions = []
    question_text = None
    choices_list = []
    correct_choice_letter = None
# -> Open quiz file (e.g., "quiz_data.txt")
    try:
        with open(file_path, 'r') as quiz_file:
# -> For each line in the file:
            for line in quiz_file:
                line = line.strip()
#   -> If line starts with "QUESTION:", store question text
                if line.startswith("QUESTION:"):
                    if question_text:
                        list_of_questions.append((question_text, choices_list, correct_choice_letter))
                    question_text = line.replace("QUESTION: ", "")
                    choices_list = []
                    correct_choice_letter = None
#   -> If line starts with "A.", "B.", etc., store choices
                elif line.startswith("A.") or line.startswith("B.") or line.startswith("C.") or line.startswith("D."):
                    choices_list.append(line[3:].strip())
#   -> If line starts with "ANSWER:", store correct answer letter
                elif line.startswith("ANSWER:"):
                    correct_choice_letter = line.replace("ANSWER: ", "").strip()
# -> After loop, add final question to list
            if question_text:
                list_of_questions.append((question_text, choices_list, correct_choice_letter))
# -> If file not found, show error and exit
    except FileNotFoundError:
        messagebox.showerror("File Not Found", f"The file '{file_path}' could not be found.")
        sys.exit(1)
# -> If list is empty, show error and exit
    if not list_of_questions:
        messagebox.showerror("Empty File", "The quiz file is empty or has formatting errors.")
        sys.exit(1)
# -> Return list of questions
    return list_of_questions

# Function: Load New Random Question
# -> Cancel existing timer if running
# -> Randomly choose a question from the loaded list
# -> Update question label on GUI
# -> Update answer buttons (A-D) with text and click handlers
# -> Clear feedback label
# -> Reset and start countdown timer

# Function: Check User Answer (on button press)
# -> Compare selected letter with correct answer
# -> If correct:
#   -> Show "✅ Correct!" message
#   -> Increase score
# -> If incorrect:
#   -> Show "❌ Incorrect" and display correct answer
# -> Disable all answer buttons
# -> Cancel countdown timer
# -> After short delay (2s), load new random question

# Function: Start Timer Countdown
# -> If time left:
#   -> Decrease by 1
#   -> Update timer label
#   -> Set timer to call itself after 1 second
# -> Else:
#   -> Show "❌ Time's up!"
#   -> Disable buttons
#   -> After 2 seconds, load next question

# GUI Setup:
# -> Create main window
# -> Set title, size, background color
# -> Load questions using load_questions_from_custom_file()
# -> Create top frame with:
#   -> Timer label (left)
#   -> Score label (right)
# -> Create large label to display question
# -> Create 4 buttons (A-D) for answer choices, styled
# -> Create feedback label (for correct/wrong feedback)
# -> Create "Next Question" button (calls load_new_random_question)

# Game Initialization:
# -> Initialize score and timer variables
# -> Call load_new_random_question to start game

# Run GUI main loop