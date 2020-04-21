import subprocess
from libqtile import widget

def gpu_temp():
    """ Get GPU temperature using nvidia-smi command """
    cmd = ["/usr/bin/nvidia-smi", "--query-gpu=temperature.gpu", "--format=csv,noheader"]
    return subprocess.check_output(cmd).decode('utf-8').strip() + "°C"

def get_volume_level():
    """  """
    cmd = ["/usr/bin/pamixer", "--get-volume"]
    return subprocess.check_output(cmd).decode('utf-8').strip()

# Important: the Memory and CPU widgets require `python-psutil` to be installed
bar_widgets = [
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
        text = "<span size='x-large'></span>",
        #text = "   ",
        font = 'KoHo'
    ),
    widget.GenPollText(
        fmt = '{}%',
        func = get_volume_level,
        update_interval = 0.2,
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
]