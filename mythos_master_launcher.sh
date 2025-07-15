#!/bin/bash
# mythos_master_launcher.sh
# 🔁 Run all MythOS Python modules alphanumerically

echo "🚀 Launching MythOS Modules in Order..."

for script in $(ls *.py | sort); do
    echo "📂 Executing: $script"
    python3 "$script"
    echo "----------------------------------------"
done

echo "✅ All modules executed."
