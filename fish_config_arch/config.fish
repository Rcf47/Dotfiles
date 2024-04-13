if status is-interactive
  ### Aliases ###
  # Navigation
  alias .. = "cd .."
  alias ... = "cd ../.."
  alias .3 = "cd ../../.."
  alias .4 = "cd ../../../.."
  alias .5 = "cd ../../../../.."
  alias cawesome="cd ~/.config/awesome"
  alias cdwn="cd ~/Downloads"
  alias ced="cd ~/Education/"
  alias cnvim="cd ~/.config/nvim"
  alias cgh="cd ~/Github"
  # Others
 alias shtd="sudo shutdown now"   # Commands to run in interactive sessions can go here
 alias ls="eza -al --color=always --group-directories-first"
 export EDITOR=/usr/bin/nvim
 fish_hybrid_key_bindings
end
