import tkinter as tkinter_module
from tkinter import messagebox
import random
import sys

# Function to load questions from the custom formatted file
def load_questions_from_custom_file(file_path):
    list_of_questions = []
    question_text = None
    choices_list = []
    correct_choice_letter = None

    try:
        with open(file_path, 'r') as quiz_file:
            for line in quiz_file:
                line = line.strip()
                if line.startswith("QUESTION:"):
                    if question_text:
                        list_of_questions.append((question_text, choices_list, correct_choice_letter))

                    question_text = line.replace("QUESTION: ", "")
                    choices_list = []
                    correct_choice_letter = None
                elif line.startswith("ANSWER:"):
                    correct_choice_letter = line.replace("ANSWER: ", "").strip()
                elif line.startswith("A.") or line.startswith("B.") or line.startswith("C.") or line.startswith("D."):
                    choices_list.append(line[3:].strip())

            if question_text:
                list_of_questions.append((question_text, choices_list, correct_choice_letter))

    except FileNotFoundError:
        messagebox.showerror("File Not Found", f"The file '{file_path}' could not be found.")
        sys.exit(1)

    if not list_of_questions:
        messagebox.showerror("Empty File", "The quiz file is empty or has formatting errors.")
        sys.exit(1)

    return list_of_questions

# Function to load a new random question and reset the timer
def load_new_random_question():
    global current_question_text, current_choices_list, correct_answer_choice_letter, timer_reference
    global remaining_time_seconds

    if timer_reference:
        quiz_window.after_cancel(timer_reference)

    current_question_text, current_choices_list, correct_answer_choice_letter = random.choice(list_of_quiz_questions)
    question_label.config(text=current_question_text)

    for button_index, choice_button in enumerate(answer_buttons):
        choice_letter = chr(65 + button_index)
        choice_button.config(
            text=f"{choice_letter}. {current_choices_list[button_index]}",
            state="normal",
            command=lambda selected_letter=choice_letter: check_user_answer(selected_letter)
        )

    feedback_label.config(text="")
    remaining_time_seconds = 15
    timer_label.config(text=f"Time remaining: {remaining_time_seconds} seconds")
    start_timer()
    