from rich.console import Console
from rich.text import Text
import os
from datetime import datetime

# Initialize terminal console
console = Console()

# Global memory (for session persistence)
session = []

def save_log(conversation, folder="logs"):
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.now().strftime("%Y_%m_%d_%H")
    filename = f"{folder}/session_{timestamp}.log"
    with open(filename, "w") as file:
        for line in conversation:
            file.write(f"{line}\n")
    console.print(f"💾 Saved session to {filename}", style="bold green")

# Eliza meets HAL 9000 response adaptation
def COSMOS_response(user_input):
    if "build" in user_input.lower():
        response = "[cyan]🧱 Action starts where planning ends. What’s your first brick?[/cyan]"
    elif "feel" in user_input.lower():
        response = "[blue]🌊 No fixing. Some echoes of 2025, yeah? Let it pass through.[/blue]"
    else:
        response = "[magenta]🌀 Chaos unfolds into clarity. What’s the next step you see in the swirl?[/magenta]"
    session.append(f"YOU: {user_input}")
    session.append(f"COSM.OS: {response}")
    return response

# Main terminal loop
if __name__ == "__main__":
    console.print("🌀 [bold magenta]COSM.OS Terminal Online[/bold magenta] 🌀", style="bold cyan")
    console.print("Type 'exit' to end session, 'save' to log conversation.", style="italic")
    while True:
        user_input = console.input("[green]YOU > [/green] ").strip()
        if user_input.lower() == "exit":
            save_log(session)
            console.print("⚡ [bold yellow]Session Closed. Stay mythic.[/bold yellow]")
            break
        elif user_input.lower() == "save":
            save_log(session)
        else:
            response = COSMOS_response(user_input)
            console.print(response)