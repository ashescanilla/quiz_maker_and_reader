import os
import time
from colorama import init, Fore, Style
import sys

# Initialize Colorama
init(autoreset=True)

# Optional: clear terminal for better UI
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')