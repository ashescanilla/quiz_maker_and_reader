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