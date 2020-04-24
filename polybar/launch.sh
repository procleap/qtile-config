#!/usr/bin/env sh

# Terminate any already running bar instances.
killall -q polybar

# Wait until polybar process has been shut down.
while pgrep -u $UID -x polybar >/dev/null; do sleep 1; done

# Launch polybar.
polybar -c ~/.config/qtile/polybar/config.ini bar &
