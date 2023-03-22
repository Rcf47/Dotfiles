#!/bin/bash

echo "install ubuntu dependencies"

# dependencies
# curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash -
# sudo add-apt-repository ppa:neovim-ppa/stable

sudo apt-get update
sudo apt-get install -y wget curl fish neovim ripgrep  nodejs unzip tar gzip neofetch fd-find tree

echo "change shell from bash to zsh"

# vars
user=`whoami`
fish=`which fish`

# shell configure
sudo chsh -s $fish $user

echo "create links for application config"

# vars
path=`pwd`

# links

ln -s $path/tmux/.tmux.conf ~/.tmux.conf

mkdir -p ~/.config
ln -s $path/nvim ~/.config/nvim

