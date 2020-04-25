
#!/bin/sh
#
# For Archlinux only. Requires`pacman-cotnrib` to be installed.
#

icon=" "

if ! updates=$(checkupdates 2> /dev/null | wc -l ); then
    updates=0
fi

echo "$icon $updates"
