from libqtile import widget, bar
from colors import CATPPUCCIN
from commands import commands


widget_defaults = dict(
    font="Fira code",
    fontsize=24,
    padding=3,
)

clock_time = widget.Clock(name="clock", format="%H:%M",
                          foreground=CATPPUCCIN["red"])
clock_date = widget.Clock(
    name="clock", format="%a, %d.%m.%Y", foreground=CATPPUCCIN["rosewater"]
)
groupbox_bar = bar.Bar(
    [
        widget.WindowCount(),
        widget.NvidiaSensors(
            format="GPU temp: {temp}°C ", foreground=CATPPUCCIN["text"]
        ),
        widget.Sep(linewidth=2, foreground=CATPPUCCIN["blue"]),
        widget.ThermalSensor(
            format="CPU: {temp:.0f}{unit} ", foreground=CATPPUCCIN["text"]
        ),
        widget.Sep(linewidth=2, foreground=CATPPUCCIN["blue"]),
        widget.Spacer(),
        # widget.TaskList(),
        widget.GroupBox(
            highlight_method="line",
            active=CATPPUCCIN["blue"],
            inactive=CATPPUCCIN["rosewater"],
            # highlight_color=[CATPPUCCIN["blue"], "#f5e0dc"],
            # block_highlight_text_color=CATPPUCCIN["blue"],
            borderwidth=4,
            this_current_screen_border=CATPPUCCIN["mauve"],
            padding=10,
            urgent_border=CATPPUCCIN["red"],
            urgent_text=CATPPUCCIN["red"],
        ),
        widget.Spacer(),
        widget.Sep(linewidth=2, foreground=CATPPUCCIN["blue"]),
        widget.Memory(
            measure_mem="G",
            format="FreeRAM: {Available: .2f} GB ",
            foreground=CATPPUCCIN["text"],
        ),
        widget.Sep(linewidth=2, foreground=CATPPUCCIN["blue"]),
        widget.CPU(
            foreground=CATPPUCCIN["text"],
            format="CPU {freq_current} GHz {load_percent:04.1f}%",
        ),
        widget.Sep(linewidth=2, foreground=CATPPUCCIN["blue"]),
        widget.WidgetBox(
            text_closed="",
            text_open=">",
            widgets=[widget.Systray()],
            name="widgetbox1",
            foreground=CATPPUCCIN["blue"],
        ),
        widget.GenPollText(
            func=commands.get_keyboard,
            update_interval=0.3,
            foreground=CATPPUCCIN["blue"],
        ),
        widget.WidgetBox(
            text_open="",
            text_closed="",
            widgets=[clock_date],
            name="widgetbox2",
        ),
        clock_time,
        widget.CurrentLayout(icon_first=True, mode="icon"),
    ],
    size=25,
    background="#10101b",
)
