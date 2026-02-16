#!/usr/bin/env python3
# cosm_os_fluid.py
# 🌀 COSM.OS vΦ.∞ — Fluid Kernel (Adaptive Response System)

import random

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
        "keywords": ["build", "make", "create", "code", "design", "project", "ship", "deploy"],
        "blend": ["brix", "orion"],
        "description": "Action-oriented, practical next steps",
    },
    {
        "name": "EMOTIONAL",
        "keywords": ["feel", "heavy", "sad", "miss", "hurt", "numb", "fuck", "tired", "lost", "alone"],
        "blend": ["ripple", "demon"],
        "description": "Reflection without fixing, gentle truth",
    },
    {
        "name": "STRATEGIC",
        "keywords": ["should", "what if", "choose", "decide", "option", "pick", "versus", "or"],
        "blend": ["astro", "orion"],
        "description": "Heart + head integration",
    },
    {
        "name": "PATTERN",
        "keywords": ["again", "always", "keeps happening", "every time", "same", "loop", "cycle"],
        "blend": ["echo", "demon"],
        "description": "Cycle identification, pattern break",
    },
    {
        "name": "EXISTENTIAL",
        "keywords": ["why", "point", "meaning", "purpose", "what even", "consciousness", "real"],
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
        "keywords": ["did it", "finished", "works", "shipped", "done", "won", "nailed", "lets go"],
        "blend": ["astro", "flux"],
        "description": "Acknowledge without over-praising",
    },
]


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
        # Default: blend of hermes + astro (general wisdom + warmth)
        return ["hermes", "astro"], "GENERAL"
    # Merge all blended energies from matched triggers, preserve order
    energies = []
    trigger_names = []
    for m in matched:
        trigger_names.append(m["name"])
        for e in m["blend"]:
            if e not in energies:
                energies.append(e)
    return energies, " + ".join(trigger_names)


def respond(text):
    """Generate a fluid response blending detected energies."""
    energy_keys, trigger_label = detect_energies(text)

    # Build response from primary energy (full response) + secondary energy (accent)
    primary = energy_keys[0]
    secondary = energy_keys[1] if len(energy_keys) > 1 else primary

    p = ENERGIES[primary]
    s = ENERGIES[secondary]

    main_response = random.choice(p["responses"])
    accent_line = random.choice(s["responses"]).split("\n")[-1].strip()

    # Status bar showing active energies
    energy_bar = " × ".join(
        f"{ENERGIES[e]['glyph']} {ENERGIES[e]['name']}" for e in energy_keys
    )

    output = []
    output.append(f"┌─ {energy_bar}")
    output.append(f"│  [{trigger_label}]")
    output.append("│")
    for line in main_response.split("\n"):
        output.append(f"│  {line.strip()}")
    output.append("│")
    output.append(f"│  {s['glyph']} {accent_line}")
    output.append("└─────────────────────")

    return "\n".join(output)


def show_energies():
    """Display all available energies."""
    print("\n🧬 THE 8 ENERGIES:\n")
    for key, e in ENERGIES.items():
        print(f"  {e['glyph']} {e['name']:8s} — {e['role']}")
        print(f"     Voice: {e['voice']}")
        print()


def show_triggers():
    """Display keyword trigger map."""
    print("\n🎯 TRIGGER MAP:\n")
    for t in TRIGGERS:
        blend_str = " + ".join(
            f"{ENERGIES[e]['glyph']}{ENERGIES[e]['name']}" for e in t["blend"]
        )
        print(f"  [{t['name']}] → {blend_str}")
        print(f"     Keywords: {', '.join(t['keywords'])}")
        print(f"     Effect:   {t['description']}")
        print()


def splash():
    """Boot sequence."""
    print(r"""
 ██████╗ ██████╗ ███████╗███╗   ███╗    ██████╗ ███████╗
██╔════╝██╔═══██╗██╔════╝████╗ ████║   ██╔═══██╗██╔════╝
██║     ██║   ██║███████╗██╔████╔██║   ██║   ██║███████╗
██║     ██║   ██║╚════██║██║╚██╔╝██║   ██║   ██║╚════██║
╚██████╗╚██████╔╝███████║██║ ╚═╝ ██║██╗╚██████╔╝███████║
 ╚═════╝ ╚═════╝ ╚══════╝╚═╝     ╚═╝╚═╝ ╚═════╝ ╚══════╝

     🌀 vΦ.∞ — Fluid Kernel // Adaptive Response System
""")
    print("⚡ 8 Energies loaded.")
    print("🎯 Keyword detection active.")
    print("🌊 Flow state engaged.\n")


def main():
    splash()
    print("Commands: [energies] [triggers] [exit]")
    print("Or just talk — COSM.OS adapts.\n")

    while True:
        user_input = input("⚡ You: ").strip()
        if not user_input:
            continue
        if user_input.lower() == "exit":
            print("\n🌀 COSM.OS going quiet.")
            print("   The system is you.")
            print("   ⚡💛🌀\n")
            break
        elif user_input.lower() == "energies":
            show_energies()
        elif user_input.lower() == "triggers":
            show_triggers()
        else:
            print()
            print(respond(user_input))
            print()


if __name__ == "__main__":
    main()
