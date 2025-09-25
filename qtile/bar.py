from libqtile import bar
from colors import CATPPUCCIN
from commands import commands
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

size = 32
widgetDecoration = {
    "decorations": [
        RectDecoration(
            colour=CATPPUCCIN["base"],
            use_widget_background=False,
            radius=10,
            filled=True,
            group=True,
        )
    ],
}
widget_defaults = dict(
    font="Fira code",
    fontsize=24,
    padding=10,
)

barConfig = {
    "size": size,
    "background": CATPPUCCIN["transparent"],
    "margin": [4, 10, 2, 10],
    "border_width": [0, 0, 0, 0],
    "border_color": [
        CATPPUCCIN["transparent"],
        CATPPUCCIN["transparent"],
        CATPPUCCIN["transparent"],
        CATPPUCCIN["transparent"],
    ],
}

clock_time = widget.Clock(
    name="clock", format="%H:%M", foreground=CATPPUCCIN["red"], **widgetDecoration
)
clock_date = widget.Clock(
    name="clock", format="%a, %d.%m.%Y", foreground=CATPPUCCIN["rosewater"]
)
tasklist = widget.TaskList(
    icon_size=size,
    fontsize=24,
    margin_y=0,
    # --- Вот ключевые изменения ---
    # spacing=0,  # Убирает текст (заголовок окна)
    parse_text=commands.parse_window_name,
    margin_x=4,  # Добавляет отступ в 4px МЕЖДУ иконками
    # --------------------------------
    # --- Очистим текст для свёрнутых/плавающих окон ---
    txt_floating="🗗",
    txt_maximized="🗖",
    txt_minimized="🗕",
    # ----------------------------------------------------
    # --- Остальные настройки для красоты ---
    padding_y=2,
    padding_x=1,
    borderwidth=2,
    highlight_method="block",  # или 'border'
    # Цвет выделения (Catppuccin Macchiato blue)
    border=CATPPUCCIN["blue"],
    # Цвет неактивных (Catppuccin Macchiato surface1)
    unfocused_border=CATPPUCCIN["surface1"],
    rounded=True,
    stretch=False,
)
groupbox_bar = bar.Bar(
    [
        widget.WindowCount(**widgetDecoration),
        widget.NvidiaSensors(
            format="GPU temp: {temp}°C ",
            foreground=CATPPUCCIN["text"],
            **widgetDecoration,
        ),
        widget.Spacer(length=10),
        widget.ThermalSensor(
            format="CPU: {temp:.0f}{unit} ",
            foreground=CATPPUCCIN["text"],
            **widgetDecoration,
        ),
        widget.Spacer(length=10),
        widget.WidgetBox(
            text_closed="",
            text_open="",
            widgets=[tasklist],
            name="widgetbox3",
            foreground=CATPPUCCIN["blue"],
        ),
        widget.Spacer(),
        widget.GroupBox(
            highlight_method="text",
            active=CATPPUCCIN["blue"],
            inactive=CATPPUCCIN["subtext1"],
            # highlight_color=[CATPPUCCIN["transparent"],
            #                 CATPPUCCIN["transparent"]],
            borderwidth=4,
            this_current_screen_border=CATPPUCCIN["mauve"],
            padding=10,
            urgent_border=CATPPUCCIN["red"],
            urgent_text=CATPPUCCIN["red"],
            **widgetDecoration,
        ),
        widget.Spacer(),
        widget.Memory(
            measure_mem="G",
            format="FreeRAM: {Available: .2f} GB ",
            foreground=CATPPUCCIN["text"],
            **widgetDecoration,
        ),
        widget.Spacer(length=10),
        widget.CPU(
            foreground=CATPPUCCIN["text"],
            format="CPU {freq_current} GHz {load_percent:04.1f}%",
            **widgetDecoration,
        ),
        widget.Spacer(length=10),
        widget.WidgetBox(
            text_closed="",
            text_open=">",
            widgets=[widget.Systray()],
            name="widgetbox1",
            foreground=CATPPUCCIN["blue"],
            **widgetDecoration,
        ),
        widget.GenPollText(
            func=commands.get_keyboard,
            update_interval=0.3,
            foreground=CATPPUCCIN["blue"],
            **widgetDecoration,
        ),
        widget.WidgetBox(
            text_open="",
            text_closed="",
            widgets=[clock_date],
            name="widgetbox2",
            **widgetDecoration,
        ),
        clock_time,
        widget.CurrentLayout(icon_first=True, mode="icon", **widgetDecoration),
    ],
    **barConfig,
)
