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
def load_new_random_question():
    global current_question_text, current_choices_list, correct_answer_choice_letter, timer_reference
    global remaining_time_seconds
# -> Cancel existing timer if running
    if timer_reference:
        quiz_window.after_cancel(timer_reference)
# -> Randomly choose a question from the loaded list
    current_question_text, current_choices_list, correct_answer_choice_letter = random.choice(list_of_quiz_questions)
# -> Update question label on GUI
    question_label.config(text=current_question_text)
# -> Update answer buttons (A-D) with text and click handlers
    for button_index, choice_button in enumerate(answer_buttons):
        choice_letter = chr(65 + button_index)
        choice_button.config(
            text=f"{choice_letter}. {current_choices_list[button_index]}",
            state="normal",
            command=lambda selected_letter=choice_letter: check_user_answer(selected_letter)
        )
# -> Clear feedback label
    feedback_label.config(text="")
# -> Reset and start countdown timer
    remaining_time_seconds = 15
    timer_label.config(text=f"Time remaining: {remaining_time_seconds} seconds")
    start_timer()

# Function: Check User Answer (on button press)
def check_user_answer(selected_letter):
    global timer_reference, score_counter
# -> Compare selected letter with correct answer
    if selected_letter == correct_answer_choice_letter:
# -> If correct:
#   -> Show "✅ Correct!" message
#   -> Increase score
        feedback_label.config(text="✅ Correct!", fg="blue", font=("Arial", 16, "bold"))
        score_counter += 1
        score_label.config(text=f"Score: {score_counter}")
    else:
# -> If incorrect:
#   -> Show "❌ Incorrect" and display correct answer
        correct_index = ord(correct_answer_choice_letter) - 65
        correct_answer_text = current_choices_list[correct_index]
        feedback_label.config(
            text=f"❌ Incorrect. The correct answer is: {correct_answer_choice_letter}. {correct_answer_text}",
            fg="red", font=("Arial", 16, "bold")
        )
# -> Disable all answer buttons
    for answer_button in answer_buttons:
        answer_button.config(state="disabled")
# -> Cancel countdown timer
    if timer_reference:
        quiz_window.after_cancel(timer_reference)
# -> After short delay (2s), load new random question
    quiz_window.after(2000, load_new_random_question)

# Function: Start Timer Countdown
def start_timer():
    global remaining_time_seconds, timer_reference
# -> If time left:
#   -> Decrease by 1
#   -> Update timer label
#   -> Set timer to call itself after 1 second
    if remaining_time_seconds > 0:
        remaining_time_seconds -= 1
        timer_label.config(text=f"Time remaining: {remaining_time_seconds} seconds")
        timer_reference = quiz_window.after(1000, start_timer)
    else:
# -> Else:
#   -> Show "❌ Time's up!"
#   -> Disable buttons
#   -> After 2 seconds, load next question
        feedback_label.config(text="❌ Time's up! Moving to the next question...", fg="red", font=("Arial", 16, "bold"))
        for answer_button in answer_buttons:
            answer_button.config(state="disabled")
        quiz_window.after(2000, load_new_random_question)

# GUI Setup:
# -> Create main window
def show_start_screen():
    start_window = tkinter_module.Tk()
# -> Set title, size
    start_window = tkinter_module.Tk()
    start_window.title("Start Quiz")
    start_window.geometry("700x600")
    start_window.resizable(False, False)

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