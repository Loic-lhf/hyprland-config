#!/usr/bin/env bash

current=$(hyprctl -j getoption general:layout | jq -r '.str')

echo "$current"

if [ "$current" = "dwindle" ]; then
    hyprctl keyword general:layout "master"
    notify-send -a "Hyprland" "  Switched to master layout"
else
    hyprctl keyword general:layout "dwindle"
    notify-send -a "Hyprland" " Switched to dwindle layout"
fi