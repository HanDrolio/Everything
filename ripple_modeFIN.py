#!/usr/bin/env python3

import os
from datetime import datetime
import glob

# === Config ===
SAVE_DIR = "/home/calderonmode99/MythOS/logs/ripple/"
FILENAME_PREFIX = "ripple_entry"

MOOD_GLYPHS = {
    "💧": "calm",
    "🌊": "emotional",
    "🌌": "reflective",
    "🧠": "thoughtful",
    "🎭": "dramatic",
    "🛸": "detached",
    "🧃": "nostalgic",
    "🔥": "intense"
}

EMOTICON_MAP = {
    ":)": "💧",
    ":(": "🌊",
    "._.": "🌌",
    "._-": "🛸",
    ":D": "🧃",
    ">:(": "🔥",
    ":|": "🧠",
    ":P": "🎭"
}

NIGHT_GLYPHS = ["🌖", "🌗", "🌘"]

RIPPLE_SUMMARIES = {
    "💧": "You’re entering a place of stillness. Let the calm speak.",
    "🌊": "Big waves of emotion. Ride them, don’t fight them.",
    "🌌": "You’re stargazing inside your own mind. Reflect deeply.",
    "🧠": "A mental storm brews — but it’s rich with insight.",
    "🎭": "Your inner theater is alive. Witness it with curiosity.",
    "🛸": "You’re observing from afar — sometimes distance brings truth.",
    "🧃": "Nostalgia’s sweet, but don’t drown in it. Sip, don’t chug.",
    "🔥": "You’re in the fire. Burn smart. Forge something new."
}

def prism_art(glyph):
    echo = MOOD_GLYPHS.get(glyph, 'Unknown')
    summary = RIPPLE_SUMMARIES.get(glyph, 'Processing emotions...')
    return (
        f"*** MIND PRISM ***\n"
        f"  {glyph}   {glyph}   {glyph}\n"
        f"    \\   |   /\n"
        f"     \\  |  /\n"
        f"      \\ | /\n"
        f"       \\|/\n"
        f"    — 💎 —\n"
        f"       /|\\\n"
        f"      / | \\\n"
        f"     /  |  \\\n"
        f"    /   |   \\\n"
        f"  {glyph}   {glyph}   {glyph}\n"
        f"💠 Glyph Echo: {echo}\n"
        f"🧠 Ripple Summary: {summary}\n"
    )

# Create save dir if missing
os.makedirs(SAVE_DIR, exist_ok=True)

def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def save_entry(mood, entry):
    timestamp = get_timestamp()
    filename = f"{FILENAME_PREFIX}_{timestamp}.rpl"
    path = os.path.join(SAVE_DIR, filename)
    with open(path, "w") as f:
        f.write(f"🧠 Mood: {mood} ({MOOD_GLYPHS[mood]})\n")
        f.write(f"🕒 Timestamp: {timestamp}\n")
        f.write(f"📜 Entry:\n{entry.strip()}\n")
        f.write("🛰️ Echo: " + " ".join(NIGHT_GLYPHS) + "\n")
        f.write("🔐🔏 Myth.OS Log Complete\n")
    print(f"\n💾 Saved to {path}")
    print("💧🌊💧🌊🌌 Ripple.lite entry logged.\n")
    print(prism_art(mood))

def list_entries():
    files = sorted(glob.glob(os.path.join(SAVE_DIR, "*.rpl")), reverse=True)
    if not files:
        print("📭 No ripple entries found.")
        return
    print("\n📂 Ripple Archive:")
    for i, file in enumerate(files[:5], 1):
        print(f"{i}. {os.path.basename(file)}")
    print()

def read_entry(filename):
    path = os.path.join(SAVE_DIR, filename)
    if not os.path.isfile(path):
        print(f"❌ File not found: {filename}")
        return
    print(f"\n📖 Reading: {filename}\n" + "═" * 40)
    with open(path, "r") as f:
        content = f.read()
        print(content)
        for glyph in MOOD_GLYPHS:
            if glyph in content:
                print(prism_art(glyph))
    print("═" * 40 + "\n📚 End of ripple log.\n")

def main():
    print("⌨️ Ripple.lite Typewriter — Emote Mode Enabled")
    while True:
        print("\nOptions: [write] [list] [read <#>] [exit]")
        command = input("🧠 Mode: ").strip()

        if command == 'exit':
            print("👋 Peace out ripple walker.")
            break
        elif command == 'list':
            list_entries()
        elif command.startswith('read '):
            try:
                index = int(command.split()[1]) - 1
                files = sorted(glob.glob(os.path.join(SAVE_DIR, "*.rpl")), reverse=True)
                if 0 <= index < len(files):
                    read_entry(os.path.basename(files[index]))
                else:
                    print("❌ Invalid ripple number.")
            except:
                print("❌ Usage: read <number>")
        elif command == 'write':
            emo = input("🙂 Your emoticon (e.g. :) :( ._-) → ").strip()
            mood = EMOTICON_MAP.get(emo)
            if not mood:
                print("⚠️ Invalid emoticon. Try one of: " + " ".join(EMOTICON_MAP.keys()))
                continue
            entry = input("📝 Your ripple thought: ")
            save_entry(mood, entry)
        else:
            print("❓ Unknown command. Use: write, list, read <#>, exit.")

if __name__ == "__main__":
    main()
