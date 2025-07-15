# rainbow_ripple_journal.py
# 🌈 Ripple Journal — Rainbow CLI Edition

import datetime
import sys

# ANSI color codes for rainbow effect
colors = [
    "\033[91m",  # Red
    "\033[93m",  # Yellow
    "\033[92m",  # Green
    "\033[96m",  # Cyan
    "\033[94m",  # Blue
    "\033[95m",  # Magenta
]

RESET = "\033[0m"

def print_rainbow(text):
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        sys.stdout.write(color + char + RESET)
    print()

def log_entry():
    print_rainbow("🌈 Welcome to Ripple Journal — Rainbow Edition 🌈")
    mood = input("💭 Mood: ")
    thought = input("📝 Your ripple thought: ")

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    entry = f"[{timestamp}] Mood: {mood}\nThought: {thought}\n"

    with open("rainbow_ripple_log.txt", "a") as f:
        f.write(entry + "\n")

    print_rainbow("✅ Entry saved. Keep rippling.")

if __name__ == "__main__":
    log_entry()
