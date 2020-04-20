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

groups = [Group(str(i)) for i in range(1, 10)]

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
        margin     = 10,
        ratio      = 0.6
    ),
    layout.Max(),
    layout.Stack(
        num_stacks = 2
    ),
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

widget_defaults = dict(
    font='sans',
    fontsize=14,
    padding=3,
)
extension_defaults = widget_defaults.copy()

def gpu_temp():
    """ Get GPU temperature using nvidia-smi command """
    cmd = ["/usr/bin/nvidia-smi", "--query-gpu=temperature.gpu", "--format=csv,noheader"]
    return subprocess.check_output(cmd).decode('utf-8').strip() + "°C"

screens = [
    Screen(
        # Important: the Memory and CPU widgets require `python-psutil` to be installed
        top=bar.Bar(
            [
                widget.Sep(
                    linewidth = 0,
                    padding = 5,
                ),
                widget.CurrentLayoutIcon(
                    scale = 0.7,
                ),
                widget.GroupBox(),
                widget.Prompt(),
                widget.WindowName(),
                widget.Systray(),
                widget.Sep(
                    linewidth = 0,
                    padding = 7,
                ),
                widget.TextBox(
                    text = '<span size="x-large"></span>',
                    font = 'KoHo'
                ),
                widget.CPU(
                    format = '{load_percent}%'
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 7,
                ),
                widget.TextBox(
                    text = "<span size='large'></span>",
                    font = 'KoHo'
                ),
                widget.TextBox("CPU"),
                widget.ThermalSensor(
                    tag_sensor = 'Package id 0', # CPU
                    threshold = 75,
                ),
                widget.GenPollText(
                    fmt = 'GPU {}',
                    func = gpu_temp,
                    update_interval = 1,
                ),
                widget.TextBox("NVME"),
                widget.ThermalSensor(
                    tag_sensor = 'Sensor 2', # NVME
                    threshold = 75,
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 7,
                ),
                widget.TextBox(
                    text = "<span size='x-large'></span>",
                    font = 'KoHo'
                ),
                widget.Memory(
                    format = '{MemUsed}M'
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 7,
                ),
                widget.TextBox(
                    text = "",
                    font = 'KoHo'
                ),
                widget.Clock(
                    format = '%I:%M %p',
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 11,
                ),
            ],
            35,
            background = '#263238',
        ),
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
    {'wmclass': 'confirmreset'}, # gitk
    {'wmclass': 'makebranch'},   # gitk
    {'wmclass': 'maketag'},      # gitk
    {'wname'  : 'branchdialog'}, # gitk
    {'wname'  : 'pinentry'},     # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
    {'wmclass': 'keepass2'},     # KeePass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

# Hooks

# Autostart applications
@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/scripts/autostart.sh')
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
