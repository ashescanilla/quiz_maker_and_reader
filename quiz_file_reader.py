# Import necessary modules:
# -> os (for file and path handling)
# -> tkinter as tkinter_module (GUI framework)
# -> messagebox from tkinter (for showing alert dialogs)
# -> PIL.Image and PIL.ImageTk (for opening and displaying images)
# -> random (for selecting random questions)
# -> sys (for exiting the program if an error occurs)
import os
import tkinter as tkinter_module
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import sys

# Define function to load questions from a text file:
# -> Reads file line by line and parses question, choices, and answer
# -> If file not found, show error and exit
# -> If no valid questions, show error and exit
def load_questions_from_custom_file(file_path):
# Initialize empty list to store questions
    list_of_questions = []
# Temporary variables to hold parsed content
    question_text = None
    choices_list = []
    correct_choice_letter = None

    try:
# Open file in read mode
        with open(file_path, 'r') as quiz_file:
            for line in quiz_file:
                line = line.strip()
# Check if line starts with "QUESTION:"
                if line.startswith("QUESTION:")
# If question already parsed, add it to list
                    if question_text:
                        list_of_questions.append((question_text, choices_list, correct_choice_letter))
# Store new question and reset choices
                    question_text = line.replace("QUESTION: ", "")
                    choices_list = []
                    correct_choice_letter = None
# Check if line contains the correct answer
                elif line.startswith("ANSWER:"):
                    correct_choice_letter = line.replace("ANSWER: ", "").strip()
# Check if line contains a choice (A., B., C., or D.)
                elif line.startswith(("A.", "B.", "C.", "D.")):
                    choices_list.append(line[3:].strip())
# After loop, add the last question
            if question_text:
                list_of_questions.append((question_text, choices_list, correct_choice_letter))
    except FileNotFoundError:
# Show error if file is not found
        messagebox.showerror("File Not Found", f"The file '{file_path}' could not be found.")
        sys.exit(1)
# Check if no questions were parsed
    if not list_of_questions:
        messagebox.showerror("Empty File", "The quiz file is empty or has formatting errors.")
        sys.exit(1)
    return list_of_questions
# Define function to load and display a new random question
def load_new_random_question():
# Declare global variables used in this function
    global current_question_text, current_choices_list, correct_answer_choice_letter, timer_reference
    global remaining_time_seconds
# Cancel any running timer
    if timer_reference:
        quiz_window.after_cancel(timer_reference)
# Pick a random question
    current_question_text, current_choices_list, correct_answer_choice_letter = random.choice(list_of_quiz_questions)
# Display question text
    question_label.config(text=current_question_text)
# Display each answer choice with corresponding letter (A-D)
    for button_index, choice_button in enumerate(answer_buttons):
        choice_letter = chr(65 + button_index)
        choice_button.config(
            text=f"{choice_letter}. {current_choices_list[button_index]}",
            state="normal",
            command=lambda selected_letter=choice_letter: check_user_answer(selected_letter)
        )
# Clear previous feedback
    feedback_label.config(text="")
# Reset and show timer
    remaining_time_seconds = 15
    timer_label.config(text=f"Time remaining: {remaining_time_seconds} seconds")
    start_timer()
# Define function to check user's selected answer
def check_user_answer(selected_letter):
    global timer_reference, score_counter
# If answer is correct
    if selected_letter == correct_answer_choice_letter:
        feedback_label.config(text="✅ Correct!", fg="blue", font=("Arial", 16, "bold"))
        score_counter += 1
        score_label.config(text=f"Score: {score_counter}")
    else:
# Show correct answer if user was wrong
        correct_index = ord(correct_answer_choice_letter) - 65
        correct_answer_text = current_choices_list[correct_index]
        feedback_label.config(
            text=f"❌ Incorrect. The correct answer is: {correct_answer_choice_letter}. {correct_answer_text}",
            fg="red", font=("Arial", 16, "bold")
        )
# Disable all answer buttons
    for answer_button in answer_buttons:
        answer_button.config(state="disabled")
# Cancel timer and load next question after delay
    if timer_reference:
        quiz_window.after_cancel(timer_reference)
    quiz_window.after(2000, load_new_random_question)
# Define function to start the countdown timer
def start_timer():
    global remaining_time_seconds, timer_reference
    if remaining_time_seconds > 0:
# Decrease time and update label
        remaining_time_seconds -= 1
        timer_label.config(text=f"Time remaining: {remaining_time_seconds} seconds")
# Call start_timer again after 1 second
        timer_reference = quiz_window.after(1000, start_timer)
    else:
# Time ran out, show timeout message and disable buttons
        feedback_label.config(text="❌ Time's up! Moving to the next question...", fg="red", font=("Arial", 16, "bold"))
        for answer_button in answer_buttons:
            answer_button.config(state="disabled")
# Load new question after 2 seconds
        quiz_window.after(2000, load_new_random_question)
# Define function to show the start screen of the app
def show_start_screen():
    start_window = tkinter_module.Tk()
# -> Set window title
    start_window.title("Start Quiz")
# -> Set window size
    start_window.geometry("700x600")
# -> Disable window resizing
    start_window.resizable(False, False)
# Load background image safely
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, "quiz_background.jpg")
    try:
        bg_image = Image.open(image_path)
        bg_image = bg_image.resize((700, 600), Image.Resampling.LANCZOS)
        background = ImageTk.PhotoImage(bg_image)
# Set image as background
        bg_label = tkinter_module.Label(start_window, image=background)
# -> Prevent garbage collection
        bg_label.image = background
        bg_label.place(x=0, y=0, relwidth=1, relheight=1)
    except FileNotFoundError:
# If image not found, use plain background
        messagebox.showwarning("Image Missing", f"Background image not found at:\n{image_path}\nUsing plain background.")
        start_window.configure(bg="#f0f0f0")
# Define function to start the quiz
    def start_quiz():
        start_window.destroy()
        launch_quiz()
# Create "Start Quiz" button
    start_button = tkinter_module.Button(
        start_window, text="Start Quiz", font=("Arial", 16),
        bg="#008CBA", fg="white", activebackground="#005F8E",
        width=20, height=2, command=start_quiz
    )
    start_button.place(relx=0.5, rely=0.85, anchor="center")
    start_window.mainloop()
# Define function to launch quiz window
def launch_quiz():
    global quiz_window, question_label, answer_buttons, feedback_label
    global timer_label, score_label, remaining_time_seconds, timer_reference, score_counter
    global list_of_quiz_questions
    def handle_window_close():
# Ask confirmation on window close

# Create main quiz window

# -> Set title

# -> Set size

# Load quiz questions from file

# Create top info frame

# Create timer label (left side)

# Create score label (right side)

# Create question label

# Create styled answer buttons (A-D)

# Create feedback label

# Create "Next Question" button

# Create "Exit" button

# Initialize game variables

# -> Start quiz

# -> Start event loop

# Start the application