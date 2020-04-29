import os

from libqtile.config import Key
from libqtile.lazy import lazy

# dynamically build path to powermenu.sh script
powermenu = "/usr/bin/bash " + os.path.expanduser('~/.config/qtile/scripts/powermenu.sh')

mod = "mod4"
keys = [
    # Switch between windows in current stack pane
    Key([mod], "k", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "Down", lazy.layout.down(),
        desc="Move focus down in stack pane"),
    Key([mod], "j", lazy.layout.up(),
        desc="Move focus up in stack pane"),
    Key([mod], "Up", lazy.layout.up(),
        desc="Move focus up in stack pane"),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "control"], "Down", lazy.layout.shuffle_down(),
        desc="Move window down in current stack "),
    Key([mod, "control"], "j", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),
    Key([mod, "control"], "Up", lazy.layout.shuffle_up(),
        desc="Move window up in current stack "),

    # Volume controls
    Key([], "XF86AudioRaiseVolume", lazy.spawn("/usr/bin/pamixer --increase 2"),
        desc="Increase volume "),
    Key([], "XF86AudioLowerVolume", lazy.spawn("/usr/bin/pamixer --decrease 2"),
        desc="Decrease volume "),
    Key([], "XF86AudioMute", lazy.spawn("/usr/bin/pamixer --toggle-mute"),
        desc="Mute volume "),

    # Move to next and previous workspaces/groups
    Key([mod, "control"], "Right", lazy.screen.next_group(),
        desc="Move to the next workspace/group "),
    Key([mod, "control"], "Left", lazy.screen.prev_group(),
        desc="Move to the previous workspace/group "),

    # MonadTall specific
    Key([mod, "control"], "f", lazy.layout.flip(),
        desc="Flip layout left/right "),
    Key([mod], "i", lazy.layout.grow(),
        desc="Increase window size "),
    Key([mod], "m", lazy.layout.shrink(),
        desc="Decrease window size "),
    Key([mod], "n", lazy.layout.normalize(),
        desc="Normalize (i.e. reset windows back to their regular size) "),
    Key([mod], "o", lazy.layout.maximize(),
        desc="Maximize window size "),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next(),
        desc="Switch window focus to other pane(s) of stack"),

    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(),
        desc="Toggle between layouts"),

    # Kill window
    Key([mod], "w", lazy.window.kill(),
        desc="Kill focused window"),

    # Restart/exit Qtile
    Key([mod, "control"], "r", lazy.restart(),
        desc="Restart qtile"),
    Key([mod, "control"], "q", lazy.shutdown(),
        desc="Shutdown qtile"),

    # Toggle window floating mode on/off
    Key([mod, "control"], "f", lazy.window.toggle_floating(),
        desc="Toggle window floating mode on/off "),

    # Toggle window fullscreen on/off
    Key([mod], "f", lazy.window.toggle_fullscreen(),
        desc="Toggle window fullscreen on/off "),

    #
    # Application launchers
    #

    # Terminal
    Key([mod], "Return", lazy.spawn("alacritty"),
        desc="Launch terminal"),

    # File manager
    Key([mod], "s", lazy.spawn("thunar"),
        desc="Launch file manager "),

    # Powermenu
    Key([mod, "control"], "l", lazy.spawn(powermenu),
        desc="Launch powermenu "),

    # Rofi launcher
    Key([mod], "d", lazy.spawn("/usr/bin/rofi -show drun -config ~/.config/qtile/rofi/launcher.rasi"),
        desc="Spawn rofi in drun mode"),
]
