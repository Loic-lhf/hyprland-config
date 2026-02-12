#
# ~/.bash_profile
#

export PATH=/home/loic-lhf/.local/bin:~/.npm-global/bin:$PATH
export QT_QPA_PLATEFORMTHEME=gtk3

[[ -f ~/.bashrc ]] && . ~/.bashrc

if [ -z "$WAYLAND_DISPLAY" ] && [ "$XDG_VTNR" -eq 1 ]; then
	exec start-hyprland
fi

# >>> juliaup initialize >>>

# !! Contents within this block are managed by juliaup !!

case ":$PATH:" in
    *:/home/loic-lhf/.juliaup/bin:*)
        ;;

    *)
        export PATH=/home/loic-lhf/.juliaup/bin${PATH:+:${PATH}}
        ;;
esac

# <<< juliaup initialize <<<
