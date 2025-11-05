#
# ~/.bashrc
#

# eval "$(starship init bash)"

# fastfetch --logo ~/.config/fastfetch/my-logo.txt
fortune | cowsay -f eyes
# If not running interactively, don't do anything
[[ $- != *i* ]] && return

if [ -f "$HOME/.cache/wal/colors.sh" ]; then
    . "$HOME/.cache/wal/colors.sh"
fi

alias ls='ls --color=auto'
alias grep='grep --color=auto'
PS1='[\u@\h \W]\$ '
export PATH="$PATH:$HOME/.local/bin"

# >>> conda initialize >>>
# !! Contents within this block are managed by 'conda init' !!
__conda_setup="$('/home/loic-lhf/miniconda3/bin/conda' 'shell.bash' 'hook' 2> /dev/null)"
if [ $? -eq 0 ]; then
    eval "$__conda_setup"
else
    if [ -f "/home/loic-lhf/miniconda3/etc/profile.d/conda.sh" ]; then
        . "/home/loic-lhf/miniconda3/etc/profile.d/conda.sh"
    else
        export PATH="/home/loic-lhf/miniconda3/bin:$PATH"
    fi
fi
unset __conda_setup
# <<< conda initialize <<<

