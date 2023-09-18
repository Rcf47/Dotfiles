if status is-interactive
alias ncal="ncal -b"
alias shtd="sudo shutdown now"
alias dwprettier ="wget https://github.com/Rcf47/JavaScript/blob/main/experiments/prettier_Eslint/.prettierrc.json"
alias dwprettierignore ="wget https://github.com/Rcf47/JavaScript/blob/main/experiments/prettier_Eslint/.prettierignore"
export EDITOR=/snap/bin/nvim
#alt+f for exact find
bind \ef ~/Programms/scripts/findWithFzf.sh
#alt+d just find
bind \ed ~/Programms/scripts/findWithFzfnotExact.sh
zoxide init fish | source
end

# bun
set --export BUN_INSTALL "$HOME/.bun"
set --export PATH $BUN_INSTALL/bin $PATH
