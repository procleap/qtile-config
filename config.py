#
# ~/.config/qtile/config.py
#

import os
import subprocess

from libqtile.config import Key, Screen, Group, Drag, Click
from libqtile.lazy import lazy
from libqtile import layout, bar, widget
from libqtile.config import hook

from typing import List  # noqa: F401

from keys import keys, mod
from quake import QuakeTerm, QuakeKey

groups = [Group(str(i)) for i in range(1, 6)]

for i in groups:
    keys.extend([
        # mod1 + letter of group = switch to group
        Key([mod], i.name, lazy.group[i.name].toscreen(),
            desc="Switch to group {}".format(i.name)),

        # mod1 + shift + letter of group = switch to & move focused window to group
        Key([mod, "shift"], i.name, lazy.window.togroup(i.name, switch_group=True),
            desc="Switch to & move focused window to group {}".format(i.name)),
        # Or, use below if you prefer not to switch to that group.
        # # mod1 + shift + letter of group = move focused window to group
        # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
        #     desc="move focused window to group {}".format(i.name)),
    ])

layouts = [
    layout.MonadTall(
        border_focus='#7B1FA2',
        margin=10,
        ratio=0.6,
        border_width=3,
        single_border_width=3,
    ),
    layout.Max(),
    #layout.Stack(),
    # Try more layouts by unleashing below layouts.
    # layout.Bsp(),
    # layout.Columns(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

# Append Quake terminal and key binding to groups and keys respectively.
quake_term = QuakeTerm()
quake_key = QuakeKey()
groups += quake_term.init_quaketerm()
keys += quake_key.init_quake_keybinding()

screens = [
    Screen(
        top=bar.Gap(40),  # reserve space for polybar.
    ),
]

# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    # Run the utility of `xprop` to see the wm class and name of an X client.
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},    # gitk
    {'wmclass': 'maketag'},       # gitk
    {'wname': 'branchdialog'},    # gitk
    {'wname': 'pinentry'},        # GPG key password entry
    {'wmclass': 'ssh-askpass'},   # ssh-askpass
    {'wmclass': 'keepass2'},      # KeePass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# Hooks

# Autostart applications
@hook.subscribe.startup_once
def startup_once():
    home = os.path.expanduser('~/.config/qtile/scripts/autostart.sh')
    subprocess.call([home])

# Restart polybar when Qtile is restarted
@hook.subscribe.startup
def startup():
    home = os.path.expanduser('~/.config/qtile/polybar/launch.sh')
    subprocess.call([home])

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
