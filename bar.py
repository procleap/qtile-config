import subprocess
from libqtile import widget


def separator(padding):
    """ Return a pre-customized separator widget """
    return widget.Sep(
        linewidth=0,
        padding=padding,
    )


def gpu_temp():
    """ Get GPU temperature using nvidia-smi command """
    cmd = ["/usr/bin/nvidia-smi",
           "--query-gpu=temperature.gpu", "--format=csv,noheader"]
    return subprocess.check_output(cmd).decode('utf-8').strip() + "°C"


# Widgets requirements:
# - Both Memory and CPU  require `python-psutil` to be installed
# - Volume requires amixer (from `alsa-utils`) to be installed
bar_widgets = [
    separator(5),
    widget.CurrentLayoutIcon(
        scale=0.7,
    ),
    widget.GroupBox(),
    widget.WindowName(),
    separator(7),
    widget.TextBox(
        text='<span size="x-large"></span>',
        font='KoHo'
    ),
    widget.CPU(
        format='{load_percent}%'
    ),
    separator(7),
    widget.TextBox(
        text="<span size='large'></span>",
        font='KoHo'
    ),
    widget.TextBox("CPU"),
    widget.ThermalSensor(
        tag_sensor='Package id 0',  # CPU
        threshold=75,
    ),
    widget.GenPollText(
        fmt='GPU {}',
        func=gpu_temp,
        update_interval=1,
    ),
    widget.TextBox("NVME"),
    widget.ThermalSensor(
        tag_sensor='Sensor 2',  # NVME
        threshold=75,
    ),
    separator(7),
    widget.TextBox(
        text="<span size='x-large'></span>",
        font='KoHo'
    ),
    widget.Memory(
        format='{MemUsed}M'
    ),
    separator(7),
    widget.TextBox(
        text="<span size='x-large'></span>",
        font='KoHo'
    ),
    widget.Volume(
        step=5,
    ),
    separator(7),
    widget.Systray(),
    widget.Sep(
        linewidth=0,
        padding=7,
    ),
    widget.TextBox(
        text="",
        font='KoHo'
    ),
    widget.Clock(
        format='%I:%M %p',
    ),
    separator(10),
]
