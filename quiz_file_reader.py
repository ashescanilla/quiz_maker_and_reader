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

# Check if line contains the correct answer

# Check if line contains a choice (A., B., C., or D.)

# After loop, add the last question

# Show error if file is not found

# Check if no questions were parsed

# Define function to load and display a new random question

# Declare global variables used in this function

# Cancel any running timer

# Pick a random question

# Display question text

# Display each answer choice with corresponding letter (A-D)

# Clear previous feedback

# Reset and show timer

# Define function to check user's selected answer

# If answer is correct

# Show correct answer if user was wrong

# Disable all answer buttons

# Cancel timer and load next question after delay

# Define function to start the countdown timer

# Decrease time and update label

# Call start_timer again after 1 second

# Time ran out, show timeout message and disable buttons

# Load new question after 2 seconds

# Define function to show the start screen of the app

# -> Set window title

# -> Set window size

# -> Disable window resizing

# Load background image safely

# Set image as background

# -> Prevent garbage collection

# If image not found, use plain background

# Define function to start the quiz

# Create "Start Quiz" button

# Define function to launch quiz window

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