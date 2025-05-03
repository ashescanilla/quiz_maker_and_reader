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

# Function to check if the selected option is correct
def check_user_answer(selected_letter):
    global timer_reference, score_counter

    if selected_letter == correct_answer_choice_letter:
        feedback_label.config(text="✅ Correct!", fg="blue", font=("Arial", 16, "bold"))
        score_counter += 1
        score_label.config(text=f"Score: {score_counter}")
    else:
        correct_index = ord(correct_answer_choice_letter) - 65
        correct_answer_text = current_choices_list[correct_index]
        feedback_label.config(
            text=f"❌ Incorrect. The correct answer is: {correct_answer_choice_letter}. {correct_answer_text}",
            fg="red", font=("Arial", 16, "bold")
        )

    for answer_button in answer_buttons:
        answer_button.config(state="disabled")

    if timer_reference:
        quiz_window.after_cancel(timer_reference)

    quiz_window.after(2000, load_new_random_question)

# Timer countdown function
def start_timer():
    global remaining_time_seconds, timer_reference

    if remaining_time_seconds > 0:
        remaining_time_seconds -= 1
        timer_label.config(text=f"Time remaining: {remaining_time_seconds} seconds")
        timer_reference = quiz_window.after(1000, start_timer)
    else:
        feedback_label.config(text="❌ Time's up! Moving to the next question...", fg="red", font=("Arial", 16, "bold"))
        for answer_button in answer_buttons:
            answer_button.config(state="disabled")
        quiz_window.after(2000, load_new_random_question)

# GUI SETUP
quiz_window = tkinter_module.Tk()
quiz_window.title("Multiple Choice Quiz")
quiz_window.geometry("700x600")
quiz_window.resizable(False, False)
quiz_window.configure(bg="#ffffff") 

# Load questions from file
quiz_file_name = "quiz_data.txt"
list_of_quiz_questions = load_questions_from_custom_file(quiz_file_name)

# Top info frame (timer and score)
top_info_frame = tkinter_module.Frame(quiz_window, bg="#ffffff") 
top_info_frame.pack(fill="x", pady=(10, 0))

timer_label = tkinter_module.Label(
    top_info_frame, text="Time remaining: 15 seconds",
    font=("Arial", 14), bg="#ffffff", anchor="w"
)
timer_label.pack(side="left", padx=20)

score_label = tkinter_module.Label(
    top_info_frame, text="Score: 0",
    font=("Arial", 14), bg="#ffffff", anchor="e"
)
score_label.pack(side="right", padx=20)
