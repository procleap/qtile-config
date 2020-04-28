import os

from libqtile.config import ScratchPad, DropDown, Key
from libqtile.command import lazy


class QuakeTerm():

    def init_quaketerm(self):
        # Terminal
        startup_script = os.path.expanduser('~/.config/qtile/scripts/quake.sh')
        terminal = "alacritty -e sh " + startup_script

        # Configuration
        height = 0.6
        width = 0.5
        x_position = 0.25
        y_position = 0
        warp_pointer = False
        on_focus_lost_hide = True
        opacity = 1

        return [
            ScratchPad("Quake",
                       dropdowns=[
                           # Drop down terminal with tmux session
                           DropDown("term",
                                    terminal,
                                    opacity=opacity,
                                    x=x_position,
                                    y=y_position,
                                    height=height,
                                    width=width,
                                    on_focus_lost_hide=on_focus_lost_hide,
                                    warp_pointer=warp_pointer),
                       ]
                       ),
        ]


class QuakeKey():
    def init_quake_keybinding(self):
        return [
            Key([], "F12",
                lazy.group["Quake"].dropdown_toggle("term")),
        ]
