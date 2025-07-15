# gui_typewriter_ripple.py
# 🧠🌈 MythOS Ripple GUI — Digital Typewriter Style (Hunter S. Thompson vibes)

import datetime
import ipywidgets as widgets
from IPython.display import display, clear_output

# Create CLI-style text box
input_box = widgets.Textarea(
    value='',
    placeholder='Type your ripple thought like a CLI terminal...',
    description='💭 Entry:',
    layout=widgets.Layout(width='100%', height='200px'),
    style={'description_width': 'initial'}
)

submit_button = widgets.Button(
    description='Log Ripple 🧠',
    button_style='success',
    tooltip='Click to log your ripple',
)

output = widgets.Output()

def save_ripple(entry):
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("gui_ripple_log.txt", "a") as f:
        f.write(f"[{timestamp}]\n{entry}\n\n")

def on_submit_click(b):
    with output:
        clear_output()
        entry = input_box.value.strip()
        if entry:
            save_ripple(entry)
            print("✅ Ripple logged.")
        else:
            print("⚠️ Nothing typed.")

submit_button.on_click(on_submit_click)

# Display GUI
display(widgets.HTML(value="<pre><b>🌌 DIGITAL TYPEWRITER — RAINBOW RIPPLES</b></pre>"))
display(input_box, submit_button, output)
