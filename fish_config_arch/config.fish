if status is-interactive
 alias shtd="sudo shutdown now"   # Commands to run in interactive sessions can go here
 alias ls="eza -al --color=always --group-directories-first"
 alias cawesome="cd ~/.config/awesome"
 alias cdwn="cd ~/Downloads"
 alias ced="cd ~/Education/"
 alias cnvim="cd ~/.config/nvim"
 alias cgh="cd ~/Github"
 export EDITOR=/usr/bin/nvim
 fish_hybrid_key_bindings
end
