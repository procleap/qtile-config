#!/bin/bash

BORDER="#1F1F1F"
SEPARATOR="#1F1F1F"
FOREGROUND="#A9ABB0"
BACKGROUND="#282C33"
BACKGROUND_ALT="#252525"
HIGHLIGHT_BACKGROUND="#4A148C"
HIGHLIGHT_FOREGROUND="#FFFFFF"

BLACK="#000000"
WHITE="#ffffff"
RED="#e53935"
GREEN="#43a047"
YELLOW="#fdd835"
BLUE="#1e88e5"
MAGENTA="#00897b"
CYAN="#00acc1"
PINK="#d81b60"
PURPLE="#8e24aa"
INDIGO="#3949ab"
TEAL="#00897b"
LIME="#c0ca33"
AMBER="#ffb300"
ORANGE="#fb8c00"
BROWN="#6d4c41"
GREY="#757575"
BLUE_GREY="#546e7a"
DEEP_PURPLE="#5e35b1"
DEEP_ORANGE="#f4511e"
LIGHT_BLUE="#039be5"
LIGHT_GREEN="#7cb342"

# Launch Rofi
MENU="$(/usr/bin/rofi -no-lazy-grab -sep "|" -dmenu -i -p 'System' \
-hide-scrollbar true \
-bw 0 \
-lines 5 \
-line-padding 10 \
-padding 20 \
-width 8 \
-xoffset -10 -yoffset 45 \
-location 3 \
-separator-style none \
-columns 1 \
-color-enabled true \
-color-window "$BACKGROUND,$BORDER,$SEPARATOR" \
-color-normal "$BACKGROUND_ALT,$FOREGROUND,$BACKGROUND_ALT,$HIGHLIGHT_BACKGROUND,$HIGHLIGHT_FOREGROUND" \
-color-active "$BACKGROUND,$MAGENTA,$BACKGROUND_ALT,$HIGHLIGHT_BACKGROUND,$HIGHLIGHT_FOREGROUND" \
-color-urgent "$BACKGROUND,$YELLOW,$BACKGROUND_ALT,$HIGHLIGHT_BACKGROUND,$HIGHLIGHT_FOREGROUND" \
<<< "  Lock|  Logout|  Suspend|  Reboot|  Shutdown")"
case "$MENU" in
  *Lock) /usr/bin/betterlockscreen -l dim ;;
  *Logout) /usr/bin/qtile-cmd -o cmd -f shutdown ;;
  *Suspend) /usr/bin/systemctl suspend ;;
  *Reboot) /usr/bin/systemctl reboot ;;
  *Shutdown) /usr/bin/systemctl -i poweroff
esac
