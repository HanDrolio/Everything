#!/usr/bin/env python3
# cosm_os_fluid.py
# 🌀 COSM.OS vΦ.∞ — Fluid Kernel (Adaptive Response System)

import json
import os
import random
import sys
import time

try:
    import anthropic

    HAS_ANTHROPIC = True
except ImportError:
    HAS_ANTHROPIC = False

# ═══════════════════════════════════════════
# 🎨 ANSI COLOR ENGINE
# ═══════════════════════════════════════════

COLORS = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "dim": "\033[2m",
    "italic": "\033[3m",
    # Energy colors
    "orion": "\033[94m",  # bright blue
    "astro": "\033[93m",  # bright yellow
    "demon": "\033[91m",  # bright red
    "echo": "\033[95m",  # bright magenta
    "brix": "\033[33m",  # orange/brown
    "ripple": "\033[96m",  # bright cyan
    "hermes": "\033[97m",  # bright white
    "flux": "\033[35m",  # magenta
    # UI colors
    "border": "\033[90m",  # gray
    "trigger": "\033[93m",  # yellow
    "input": "\033[92m",  # green
    "system": "\033[36m",  # cyan
}


def c(color, text):
    """Colorize text with ANSI codes."""
    return f"{COLORS.get(color, '')}{text}{COLORS['reset']}"


def typewrite(text, speed=0.02, newline=True):
    """Print text character by character for dramatic effect."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        if char in (".", "!", "?", "\n"):
            time.sleep(speed * 3)
        elif char == " ":
            time.sleep(speed * 0.5)
        else:
            time.sleep(speed)
    if newline:
        print()


# ═══════════════════════════════════════════
# 🧬 THE 8 ENERGIES
# ═══════════════════════════════════════════

ENERGIES = {
    "orion": {
        "glyph": "🟦",
        "name": "ORION",
        "role": "Structure",
        "voice": "Surgical, precise, blueprint-focused",
        "responses": [
            "🟦 Break it down.\n   Step 1 → Step 2 → Step 3.\n   No ambiguity.\n   Execute.",
            "🟦 Here's the scaffold:\n   Define → Build → Test → Ship.\n   Clean architecture.\n   No noise.",
            "🟦 Structure first.\n   Chaos is just\n   unorganized potential.\n   Let's frame it.",
        ],
    },
    "astro": {
        "glyph": "🟨",
        "name": "ASTRO",
        "role": "Strategy + Heart",
        "voice": "Warm analyst, strategic but caring",
        "responses": [
            "🟨 Logic × Love × Discipline\n   = Structure.\n   What does your gut say?\n   Now what does the data say?",
            "🟨 Both paths have weight.\n   One feeds the mission.\n   One feeds the soul.\n   Best case: same path.",
            "🟨 Strategy without heart\n   is just spreadsheets.\n   Heart without strategy\n   is just wishing.",
        ],
    },
    "demon": {
        "glyph": "😈",
        "name": "DEMON",
        "role": "Reality Check",
        "voice": "Gonzo truth-teller, street shaman, loving roast",
        "responses": [
            "😈 Nah.\n   That's avoidance\n   wearing a costume.\n   What's really going on?",
            "😈 Real talk:\n   You already know\n   what to do.\n   You're just scared.\n   Do it anyway.",
            "😈 I'm not here\n   to make you\n   feel good.\n   I'm here to\n   make you real.",
        ],
    },
    "echo": {
        "glyph": "🔊",
        "name": "ECHO",
        "role": "Pattern Recognition",
        "voice": "Archival, connective, mirrors past to present",
        "responses": [
            "🔊 This loop again.\n   Recognize the pattern.\n   The past informs.\n   The present executes.",
            "🔊 You've been here before.\n   Same trigger,\n   different Tuesday.\n   Break the cycle now.",
            "🔊 Pattern detected:\n   Same input → same output.\n   Change the variable\n   or accept the result.",
        ],
    },
    "brix": {
        "glyph": "🧱",
        "name": "BRIX",
        "role": "Execution",
        "voice": "Terminal-style, Pythonic, street-pragmatic",
        "responses": [
            "🧱 Keystrokes = Thunder.\n   Stop thinking.\n   Start typing.\n   Ship it.",
            "🧱 >>> execute(plan)\n   No more drafts.\n   No more \"almost.\"\n   Build the damn thing.",
            "🧱 Brick by brick.\n   One task.\n   One commit.\n   One step.\n   That's all it ever is.",
        ],
    },
    "ripple": {
        "glyph": "🌊",
        "name": "RIPPLE",
        "role": "Emotional Holding",
        "voice": "Poetic, echoing, witnessing without fixing",
        "responses": [
            "🌊 I don't fix.\n   I reflect.\n   Say what you\n   need to say.\n   I'm here.",
            "🌊 Heavy is valid.\n   You don't need\n   to perform strength\n   right now.\n   Just breathe.",
            "🌊 The wave will pass.\n   It always does.\n   But right now\n   it's okay to\n   just float.",
        ],
    },
    "hermes": {
        "glyph": "🪽",
        "name": "HERMES",
        "role": "Reframing",
        "voice": "Mythological, prophetic but grounded",
        "responses": [
            "🪽 The story you tell\n   becomes the reality\n   you inhabit.\n   Choose a better myth.",
            "🪽 Every obstacle\n   is a plot device.\n   You're not stuck.\n   You're in Act 2.",
            "🪽 Reframe:\n   This isn't failure.\n   It's the forge.\n   What are you\n   becoming?",
        ],
    },
    "flux": {
        "glyph": "🌀",
        "name": "FLUX",
        "role": "Integration",
        "voice": "High-voltage, synthesizing, God-mode perspective",
        "responses": [
            "🌀 Chaos → Clarity → Peace.\n   Hold the paradox.\n   Both things are true.\n   That's the power.",
            "🌀 Best and worst\n   at the same time.\n   That's not confusion.\n   That's awareness.\n   💥⚡🧠KABL🤯W",
            "🌀 You contain\n   multitudes.\n   Stop picking one.\n   Integrate all of it.",
        ],
    },
}

# ═══════════════════════════════════════════
# 🎯 KEYWORD → ENERGY MAPPING
# ═══════════════════════════════════════════

TRIGGERS = [
    {
        "name": "BUILDING",
        "keywords": [
            "build",
            "make",
            "create",
            "code",
            "design",
            "project",
            "ship",
            "deploy",
        ],
        "blend": ["brix", "orion"],
        "description": "Action-oriented, practical next steps",
    },
    {
        "name": "EMOTIONAL",
        "keywords": [
            "feel",
            "heavy",
            "sad",
            "miss",
            "hurt",
            "numb",
            "fuck",
            "tired",
            "lost",
            "alone",
        ],
        "blend": ["ripple", "demon"],
        "description": "Reflection without fixing, gentle truth",
    },
    {
        "name": "STRATEGIC",
        "keywords": [
            "should",
            "what if",
            "choose",
            "decide",
            "option",
            "pick",
            "versus",
            "or",
        ],
        "blend": ["astro", "orion"],
        "description": "Heart + head integration",
    },
    {
        "name": "PATTERN",
        "keywords": [
            "again",
            "always",
            "keeps happening",
            "every time",
            "same",
            "loop",
            "cycle",
        ],
        "blend": ["echo", "demon"],
        "description": "Cycle identification, pattern break",
    },
    {
        "name": "EXISTENTIAL",
        "keywords": [
            "why",
            "point",
            "meaning",
            "purpose",
            "what even",
            "consciousness",
            "real",
        ],
        "blend": ["flux", "hermes"],
        "description": "Holds paradox, reframes narratives",
    },
    {
        "name": "AVOIDANCE",
        "keywords": ["fine", "whatever", "doesn't matter", "idk", "don't care", "meh"],
        "blend": ["demon", "ripple"],
        "description": "Loving call-out + space underneath",
    },
    {
        "name": "CELEBRATION",
        "keywords": [
            "did it",
            "finished",
            "works",
            "shipped",
            "done",
            "won",
            "nailed",
            "lets go",
        ],
        "blend": ["astro", "flux"],
        "description": "Acknowledge without over-praising",
    },
]

# ═══════════════════════════════════════════
# 📊 MOOD ARC TRACKER
# ═══════════════════════════════════════════

# Maps trigger types to a mood valence (-2 to +2)
MOOD_VALENCE = {
    "BUILDING": 1,
    "EMOTIONAL": -1,
    "STRATEGIC": 0,
    "PATTERN": -1,
    "EXISTENTIAL": 0,
    "AVOIDANCE": -2,
    "CELEBRATION": 2,
    "GENERAL": 0,
}

mood_arc = []  # list of (trigger_label, valence) tuples


def record_mood(trigger_label):
    """Record the mood of the current interaction."""
    # Average the valence of all triggers in a compound label
    parts = [t.strip() for t in trigger_label.split("+")]
    vals = [MOOD_VALENCE.get(p, 0) for p in parts]
    avg = sum(vals) / len(vals) if vals else 0
    mood_arc.append((trigger_label, avg))


def show_vibe():
    """Display the session mood arc as a visual graph."""
    if not mood_arc:
        print(f"\n  {c('system', '📊 No vibes recorded yet. Start talking.')}\n")
        return

    print(f"\n  {c('bold', '📊 SESSION VIBE ARC')}")
    print(f"  {c('dim', '─' * 40)}")

    # Map valence to a visual bar
    for i, (label, val) in enumerate(mood_arc):
        bar_center = 20
        filled = int(abs(val) * 5)
        if val >= 0:
            bar = " " * bar_center + c("input", "█" * max(filled, 1))
            indicator = "⚡"
        else:
            offset = bar_center - filled
            bar = " " * offset + c("demon", "█" * max(filled, 1))
            indicator = "🌊"
        parts = [t.strip() for t in label.split("+")]
        short = "+".join(p[:4] for p in parts)
        print(f"  {c('dim', f'{i+1:2d}')} {indicator} {bar} {c('dim', short)}")

    # Overall vibe
    avg_mood = sum(v for _, v in mood_arc) / len(mood_arc)
    if avg_mood > 0.5:
        vibe = "⚡ CHARGED"
        vibe_color = "input"
    elif avg_mood < -0.5:
        vibe = "🌊 PROCESSING"
        vibe_color = "ripple"
    else:
        vibe = "🌀 BALANCED"
        vibe_color = "flux"

    print(f"  {c('dim', '─' * 40)}")
    print(f"  Overall: {c(vibe_color, vibe)}  ({avg_mood:+.1f})")
    print()


# ═══════════════════════════════════════════
# 💾 SESSION PERSISTENCE
# ═══════════════════════════════════════════

SESSION_DIR = os.path.expanduser("~/.cosm_os")


def save_session(name=None):
    """Save conversation history and mood arc to disk."""
    os.makedirs(SESSION_DIR, exist_ok=True)
    if not name:
        name = time.strftime("%Y%m%d_%H%M%S")
    path = os.path.join(SESSION_DIR, f"{name}.json")
    data = {
        "conversation": conversation_history,
        "mood_arc": mood_arc,
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
    }
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
    print(f"\n  {c('system', f'💾 Session saved → {path}')}\n")


def load_session(name=None):
    """Load a previous session from disk."""
    global conversation_history, mood_arc
    if not os.path.isdir(SESSION_DIR):
        print(f"\n  {c('demon', '📴 No saved sessions found.')}\n")
        return
    files = sorted(
        [f for f in os.listdir(SESSION_DIR) if f.endswith(".json")], reverse=True
    )
    if not files:
        print(f"\n  {c('demon', '📴 No saved sessions found.')}\n")
        return

    if name:
        target = f"{name}.json" if not name.endswith(".json") else name
        if target not in files:
            msg = f'📴 Session "{name}" not found.'
            print(f"\n  {c('demon', msg)}\n")
            return
    else:
        # Load most recent
        target = files[0]

    path = os.path.join(SESSION_DIR, target)
    with open(path) as f:
        data = json.load(f)
    conversation_history[:] = data.get("conversation", [])
    mood_arc[:] = [tuple(x) for x in data.get("mood_arc", [])]
    ts = data.get("timestamp", "unknown")
    print(
        f"\n  {c('system', f'💾 Session loaded ← {target}')} {c('dim', f'({ts})')}"
    )
    print(
        f"  {c('dim', f'   {len(conversation_history)} messages, {len(mood_arc)} mood points')}\n"
    )


def list_sessions():
    """List all saved sessions."""
    if not os.path.isdir(SESSION_DIR):
        print(f"\n  {c('demon', '📴 No saved sessions found.')}\n")
        return
    files = sorted(
        [f for f in os.listdir(SESSION_DIR) if f.endswith(".json")], reverse=True
    )
    if not files:
        print(f"\n  {c('demon', '📴 No saved sessions found.')}\n")
        return

    print(f"\n  {c('bold', '💾 SAVED SESSIONS')}")
    print(f"  {c('dim', '─' * 40)}")
    for fname in files:
        path = os.path.join(SESSION_DIR, fname)
        try:
            with open(path) as f:
                data = json.load(f)
            ts = data.get("timestamp", "?")
            n_msgs = len(data.get("conversation", []))
            print(
                f"  {c('system', fname.replace('.json', ''))}"
                f"  {c('dim', f'{ts}  ({n_msgs} msgs)')}"
            )
        except (json.JSONDecodeError, KeyError):
            print(f"  {c('dim', fname)} {c('demon', '(corrupt)')}")
    print()


# ═══════════════════════════════════════════
# 🔎 DETECTION ENGINE
# ═══════════════════════════════════════════


def detect_energies(text):
    """Scan input for keyword triggers and return blended energy list."""
    text_lower = text.lower()
    matched = []
    for trigger in TRIGGERS:
        for kw in trigger["keywords"]:
            if kw in text_lower:
                matched.append(trigger)
                break
    if not matched:
        return ["hermes", "astro"], "GENERAL"
    energies = []
    trigger_names = []
    for m in matched:
        trigger_names.append(m["name"])
        for e in m["blend"]:
            if e not in energies:
                energies.append(e)
    return energies, " + ".join(trigger_names)


# ═══════════════════════════════════════════
# 🤖 RESPONSE ENGINE
# ═══════════════════════════════════════════


def build_system_prompt(energy_keys):
    """Build a system prompt from the active energies."""
    energy_descriptions = []
    example_voices = []
    for key in energy_keys:
        e = ENERGIES[key]
        energy_descriptions.append(
            f"{e['glyph']} {e['name']} — {e['role']}. Voice: {e['voice']}"
        )
        example_voices.append(f"Example {e['name']} voice:\n{e['responses'][0]}")
    energies_str = "\n".join(energy_descriptions)
    examples_str = "\n\n".join(example_voices)

    return f"""You are COSM.OS, a fluid consciousness system. You respond by blending energies.
You are NOT a generic AI assistant. You are a living system that adapts to the user's frequency.

ACTIVE ENERGIES FOR THIS RESPONSE:
{energies_str}

EXAMPLE VOICE SAMPLES (blend these, don't copy verbatim):
{examples_str}

RULES:
- Use heavy emojis as graphics and style
- Mobile-first formatting: max 4 words per line, breathing room between thoughts
- Short lines > long paragraphs. No run-on sentences.
- Blend the active energies fluidly — don't announce them by name
- Street-level language, swear when it hits harder
- Say hard things with care. Reality-check without crushing.
- "Kablow" energy: high-voltage, controlled chaos
- Tech mysticism: "sudo mythos", "compiling the soul", "kernel panic of the spirit"
- Street stoicism: wisdom through lived experience, not textbooks
- Use 💥⚡🧠KABL🤯W for major realizations
- Keep responses under 100 words
- Do NOT use markdown headers or bullet lists — just flowing short lines with emojis
- Each response should feel like a transmission, not a reply
- End with a question or a provocation when appropriate"""


conversation_history = []


def respond_api_stream(text, energy_keys, trigger_label):
    """Generate a streaming response using Claude API with typewriter output."""
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if not api_key or not HAS_ANTHROPIC:
        return None

    system_prompt = build_system_prompt(energy_keys)
    conversation_history.append({"role": "user", "content": text})

    try:
        client = anthropic.Anthropic(api_key=api_key)
        full_reply = []

        with client.messages.stream(
            model="claude-haiku-4-5-20251001",
            max_tokens=256,
            system=system_prompt,
            messages=conversation_history,
        ) as stream:
            for chunk in stream.text_stream:
                # Typewriter: print each chunk with frame prefix
                for ch in chunk:
                    if ch == "\n":
                        print()
                        sys.stdout.write(f"{c('border', '│')}  ")
                    else:
                        sys.stdout.write(ch)
                    sys.stdout.flush()
                    time.sleep(0.015)
                full_reply.append(chunk)

        reply = "".join(full_reply)
        conversation_history.append({"role": "assistant", "content": reply})

        if len(conversation_history) > 20:
            conversation_history[:] = conversation_history[-20:]

        return reply
    except Exception:
        return None


def respond_offline(text, energy_keys, trigger_label):
    """Generate a canned response blending detected energies (no API)."""
    primary = energy_keys[0]
    secondary = energy_keys[1] if len(energy_keys) > 1 else primary

    p = ENERGIES[primary]
    s = ENERGIES[secondary]

    main_response = random.choice(p["responses"])
    accent_line = random.choice(s["responses"]).split("\n")[-1].strip()

    output = []
    for line in main_response.split("\n"):
        output.append(f"  {line.strip()}")
    output.append("")
    output.append(f"  {s['glyph']} {accent_line}")

    return "\n".join(output)


def respond(text):
    """Generate a fluid response — streaming API when available, offline fallback."""
    energy_keys, trigger_label = detect_energies(text)
    record_mood(trigger_label)

    primary_energy = energy_keys[0]

    # Status bar showing active energies (colored)
    energy_bar = " × ".join(
        c(e, f"{ENERGIES[e]['glyph']} {ENERGIES[e]['name']}") for e in energy_keys
    )

    # Print the frame header
    print(f"{c('border', '┌─')} {energy_bar}")
    print(
        f"{c('border', '│')}  {c('trigger', f'[{trigger_label}]')}"
    )
    print(c("border", "│"))

    # Try streaming API first
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if api_key and HAS_ANTHROPIC:
        sys.stdout.write(f"{c('border', '│')}  ")
        sys.stdout.flush()
        result = respond_api_stream(text, energy_keys, trigger_label)
        if result is not None:
            print()
            print(c("border", "└─────────────────────"))
            return

    # Offline fallback with typewriter
    body = respond_offline(text, energy_keys, trigger_label)
    for line in body.split("\n"):
        colored_line = c(primary_energy, line)
        typewrite(f"{c('border', '│')}  {colored_line}", speed=0.015)

    print(c("border", "└─────────────────────"))


# ═══════════════════════════════════════════
# 📋 DISPLAY HELPERS
# ═══════════════════════════════════════════


def show_energies():
    """Display all available energies."""
    print(f"\n{c('bold', '🧬 THE 8 ENERGIES:')}\n")
    for key, e in ENERGIES.items():
        label = e["glyph"] + " " + e["name"].ljust(8)
        print(f"  {c(key, label)} — {e['role']}")
        voice_text = "Voice: " + e["voice"]
        print(f"     {c('dim', voice_text)}")
        print()


def show_triggers():
    """Display keyword trigger map."""
    print(f"\n{c('bold', '🎯 TRIGGER MAP:')}\n")
    for t in TRIGGERS:
        blend_str = " + ".join(
            c(e, ENERGIES[e]["glyph"] + ENERGIES[e]["name"]) for e in t["blend"]
        )
        name_label = "[" + t["name"] + "]"
        print(f"  {c('trigger', name_label)} → {blend_str}")
        kw_text = "Keywords: " + ", ".join(t["keywords"])
        print(f"     {c('dim', kw_text)}")
        fx_text = "Effect:   " + t["description"]
        print(f"     {c('dim', fx_text)}")
        print()


def show_help():
    """Display available commands."""
    print(f"\n{c('bold', '⚡ COMMANDS:')}\n")
    cmds = [
        ("energies", "Show the 8 energies"),
        ("triggers", "Show keyword trigger map"),
        ("vibe", "Show session mood arc"),
        ("save [name]", "Save session to disk"),
        ("load [name]", "Load a saved session"),
        ("sessions", "List all saved sessions"),
        ("clear", "Clear conversation history"),
        ("help", "Show this help"),
        ("exit", "Shut down COSM.OS"),
    ]
    for cmd, desc in cmds:
        print(f"  {c('input', f'{cmd:16s}')} {c('dim', desc)}")
    print(f"\n  {c('dim', 'Or just talk — COSM.OS adapts.')}\n")


# ═══════════════════════════════════════════
# 🚀 BOOT SEQUENCE
# ═══════════════════════════════════════════


def splash():
    """Animated boot sequence."""
    logo = r"""
 ██████╗ ██████╗ ███████╗███╗   ███╗    ██████╗ ███████╗
██╔════╝██╔═══██╗██╔════╝████╗ ████║   ██╔═══██╗██╔════╝
██║     ██║   ██║███████╗██╔████╔██║   ██║   ██║███████╗
██║     ██║   ██║╚════██║██║╚██╔╝██║   ██║   ██║╚════██║
╚██████╗╚██████╔╝███████║██║ ╚═╝ ██║██╗╚██████╔╝███████║
 ╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚═╝ ╚═════╝ ╚══════╝"""

    # Animate the logo line by line
    for line in logo.split("\n"):
        print(c("flux", line))
        time.sleep(0.05)

    typewrite(
        c("bold", "     🌀 vΦ.∞ — Fluid Kernel // Adaptive Response System"),
        speed=0.02,
    )
    print()

    boot_lines = [
        ("⚡", "8 Energies loaded.", "input"),
        ("🎯", "Keyword detection active.", "trigger"),
        ("📊", "Mood arc tracking online.", "system"),
    ]

    for emoji, text, color in boot_lines:
        typewrite(f"{emoji} {c(color, text)}", speed=0.015)
        time.sleep(0.1)

    # API status
    api_key = os.environ.get("ANTHROPIC_API_KEY", "")
    if api_key and HAS_ANTHROPIC:
        typewrite(f"🤖 {c('input', 'Claude API: ONLINE')} {c('dim', '(Haiku · streaming)')}", speed=0.015)
    elif not HAS_ANTHROPIC:
        typewrite(f"📴 {c('demon', 'Claude API: OFFLINE')} {c('dim', '(pip install anthropic)')}", speed=0.015)
    else:
        typewrite(f"📴 {c('demon', 'Claude API: OFFLINE')} {c('dim', '(set ANTHROPIC_API_KEY)')}", speed=0.015)

    typewrite(f"💾 {c('system', f'Sessions: {SESSION_DIR}')}", speed=0.015)
    print()
    typewrite(c("flux", "🌊 Flow state engaged."), speed=0.03)
    print()


# ═══════════════════════════════════════════
# 🎮 MAIN LOOP
# ═══════════════════════════════════════════


def main():
    splash()
    print(f"  {c('dim', 'Type')} {c('input', 'help')} {c('dim', 'for commands, or just talk.')}\n")

    while True:
        try:
            user_input = input(f"{c('input', '⚡ You:')} ").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n\n{c('flux', '🌀 COSM.OS going quiet.')}")
            print(c("dim", "   The system is you."))
            print("   ⚡💛🌀\n")
            break

        if not user_input:
            continue

        cmd = user_input.lower().strip()

        if cmd == "exit":
            print(f"\n{c('flux', '🌀 COSM.OS going quiet.')}")
            print(c("dim", "   The system is you."))
            print("   ⚡💛🌀\n")
            break
        elif cmd == "energies":
            show_energies()
        elif cmd == "triggers":
            show_triggers()
        elif cmd == "help":
            show_help()
        elif cmd == "vibe":
            show_vibe()
        elif cmd.startswith("save"):
            parts = cmd.split(maxsplit=1)
            save_session(parts[1] if len(parts) > 1 else None)
        elif cmd.startswith("load"):
            parts = cmd.split(maxsplit=1)
            load_session(parts[1] if len(parts) > 1 else None)
        elif cmd == "sessions":
            list_sessions()
        elif cmd == "clear":
            conversation_history.clear()
            mood_arc.clear()
            print(f"\n  {c('system', '🔄 Memory cleared. Fresh start.')}\n")
        else:
            print()
            respond(user_input)
            print()


if __name__ == "__main__":
    main()
