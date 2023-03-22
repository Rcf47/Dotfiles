#!/bin/bash
# Save the tty settings and restore them on exit.
SAVED_TERM_SETTINGS="$(stty -g)"
trap "stty \"${SAVED_TERM_SETTINGS}\"" EXIT

# Force the tty (back) into canonical line-reading mode.
stty cooked echo


echo -n "Enter your exact file: "
read name
nvim $(fdfind -Hg $name ~ | fzf --preview 'batcat --color=always --style=numbers --line-range=:500 {}')
