#!/bin/sh

run() {
  if ! pgrep -f "$1" ;
  then
    "$@"&
  fi
}

run setxkbmap -layout "us,ru" -option "grp:caps_toggle,grp_led:scroll"
