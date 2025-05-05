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
# -> Initialize empty question list
# -> Open quiz file (e.g., "quiz_data.txt")
# -> For each line in the file:
#   -> If line starts with "QUESTION:", store question text
#   -> If line starts with "A.", "B.", etc., store choices
#   -> If line starts with "ANSWER:", store correct answer letter
# -> After loop, add final question to list
# -> If file not found, show error and exit
# -> If list is empty, show error and exit
# -> Return list of questions

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