#!/usr/bin/env bash

# File to store current sensitivity
STATE_FILE="$HOME/.config/hypr/scripts/sensitivity_state"

# Sensitivity levels
LEVELS=(0 0.25 0.5 1)


# Create state file if missing
if [ ! -f "$STATE_FILE" ]; then
    echo "1" > "$STATE_FILE"
fi

# Read current index
CURRENT_INDEX=$(cat "$STATE_FILE")

# Compute next index
NEXT_INDEX=$(( (CURRENT_INDEX + 1) % ${#LEVELS[@]} ))

# Apply new sensitivity
hyprctl keyword "input:sensitivity" "${LEVELS[$NEXT_INDEX]}"

# Save new index
echo "$NEXT_INDEX" > "$STATE_FILE"

# Optional: show a notification (requires notify-send)
notify-send -a "Hyprland" "  Mouse Sensitivity set to ${LEVELS[$NEXT_INDEX]}"