\
# trippy_rainbow_ripple.py
# 🧠🌈 Trippy Rainbow Ripple Journal with ASCII Vibes

import datetime
import sys
import os
import time

# ANSI rainbow colors
colors = [
    "\033[91m",  # Red
    "\033[93m",  # Yellow
    "\033[92m",  # Green
    "\033[96m",  # Cyan
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
]
RESET = "\033[0m"

def print_rainbow(text, delay=0.01):
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        sys.stdout.write(color + char + RESET)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def intro_art():
    ascii_art = r'''
    ⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣴⣶⣾⣿⣿⣿⣿⣷⣶⣤⣄⡀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⣠⣾⣿⡿⠟⠋⠁⠀⠀⠀⠀⠈⠉⠛⠿⣿⣷⣄⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⢀⣼⣿⡿⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣿⣷⡀⠀⠀⠀
    ⠀⠀⠀⠀⣼⣿⠋⠀⠀⠀🧠🌈 RAINBOW RIPPLE MODE⠀⠀⠈⣿⣧⠀⠀⠀
    ⠀⠀⠀⣸⣿⠃⠀⠀⠀⠀⠀⣀⣤⣶⣶⣶⣶⣦⣤⣀⠀⠀⠀⠸⣿⣇⠀⠀⠀
    ⠀⠀⢠⣿⡇⠀⠀⠀⠀⢀⣾⣿⡿⠛⠉⠉⠛⢿⣿⣿⣷⡀⠀⠀⣿⣿⠀⠀⠀
    ⠀⠀⣼⣿⠀⠀⠀⠀⠀⣿⣿⣷⠀⠀⠀⠀⠀⣾⣿⣿⣿⠀⠀⠀⣿⣿⠀⠀⠀
    ⠀⠀⣿⣿⠀⠀⠀⠀⠀⠹⣿⣿⣷⣦⣀⣠⣾⣿⣿⣿⠏⠀⠀⠀⣿⣿⠀⠀⠀
    '''
    print_rainbow(ascii_art, delay=0.0005)

def log_entry():
    os.system("clear")
    intro_art()
    print_rainbow("💭 Mood:", delay=0.02)
    mood = input()
    print_rainbow("📝 Your ripple thought:", delay=0.02)
    thought = input()

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] Mood: {mood}\nThought: {thought}\n"

    with open("trippy_ripple_log.txt", "a") as f:
        f.write(entry + "\n")

    print_rainbow("✅ Entry saved to trippy_ripple_log.txt. Keep melting minds...\n", delay=0.01)

if __name__ == "__main__":
    log_entry()
