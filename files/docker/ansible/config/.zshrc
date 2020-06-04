# Path to your oh-my-zsh installation.
export ZSH=~/.oh-my-zsh

ZSH_THEME="bullet-train_custom"

plugins=(docker python git)

source $ZSH/oh-my-zsh.sh

DEFAULT_USER="root"
export CLICOLOR=1
export LSCOLORS=gxfxbEaEBxxEhEhBaDaCaD
export GIT_TERMINAL_PROMPT=0
export EDITOR="vim"

setopt noflowcontrol
setopt noincappendhistory
setopt nosharehistory
setopt histexpiredupsfirst # Expire duplicate entries first when trimming history.
setopt histignoredups      # Don't record an entry that was just recorded again.
setopt histignorealldups   # Delete old recorded entry if new entry is a duplicate.
setopt histfindnodups      # Do not display a line previously found.
setopt histignorespace     # Don't record an entry starting with a space.
setopt histsavenodups      # Don't write duplicate entries in the history file.
setopt ignoreeof           # Don't exit shell on ctrl D

autoload -U +X bashcompinit && bashcompinit
export PATH="/usr/local/bin:$PATH"