import tkinter as tkinter_module
from tkinter import messagebox
from PIL import Image, ImageTk
import random
import sys

# Load questions from file
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
                elif line.startswith(("A.", "B.", "C.", "D.")):
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


