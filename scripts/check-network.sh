#!/usr/bin/bash

count=0
disconnected="睊"
wireless_connected="直"

ID="$(ip link | awk '/state UP/ {print $2}')"

while true; do
    if (ping -c 1 archlinux.org || ping -c 1 google.com || ping -c 1 github.com ) &>/dev/null; then
        echo "$wireless_connected"
    else
        echo "$disconnected"
    fi
done
