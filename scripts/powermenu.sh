#!/bin/bash

rofi_command="rofi -theme ~/.config/qtile/rofi/powermenu.rasi"

who=$(whoami)
host=$(hostname)
hostinfo="$who@$host"

# Options
lock="  Lock"
logout="  Logout"
suspend="  Suspend"
reboot="  Reboot"
shutdown="  Shutdown"

# Power menu options
options="$lock\n$logout\n$suspend\n$reboot\n$shutdown"

chosen="$(echo -e "$options" | $rofi_command -p $hostinfo -dmenu -selected-row 0)"
case $chosen in
  $lock)
    /usr/bin/betterlockscreen -l dim ;;
  $logout)
    /usr/bin/qtile-cmd -o cmd -f shutdown ;;
  $suspend)
    /usr/bin/systemctl suspend ;;
  $reboot)
    /usr/bin/systemctl reboot ;;
  $shutdown)
    /usr/bin/systemctl -i poweroff
esac
