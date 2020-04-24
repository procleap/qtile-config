#! /bin/bash

/usr/bin/nitrogen --restore &
/usr/bin/xfce4-power-manager &
/usr/bin/picom --config ~/.config/qtile/picom/picom.cfg &
/usr/bin/bash ~/.config/qtile/polybar/launch.sh &

