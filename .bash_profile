#
# ~/.bash_profile
#

export PATH=/home/loic-lhf/.local/bin:~/.npm-global/bin:$PATH
export QT_QPA_PLATEFORMTHEME=gtk3

[[ -f ~/.bashrc ]] && . ~/.bashrc

if [ -z "$WAYLAND_DISPLAY" ] && [ "$XDG_VTNR" -eq 1 ]; then
	exec Hyprland
fi
