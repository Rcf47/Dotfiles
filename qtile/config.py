import os
import subprocess

import libqtile.resources
from libqtile import bar, layout, qtile, widget, hook
from libqtile.config import Click, Drag, Key, Match, Screen
from libqtile.lazy import lazy
from groups import groups
from colors import CATPPUCCIN
from subprocess import check_output

mod = "mod4"
terminal = "kitty"
clock_time = widget.Clock(name="clock", format="%H:%M",
                          foreground=CATPPUCCIN["red"])
clock_date = widget.Clock(
    name="clock", format="%a, %d.%m.%Y", foreground=CATPPUCCIN["rosewater"]
)


class Commands:

    def get_keyboard(self):
        display_map = {
            "us": "🇺🇸 ",
            "ru": "🇷🇺 ",
        }
        keyboard = (
            check_output("xkb-switch -p",
                         shell=True).decode("utf-8").replace("\n", "")
        )

        return display_map[keyboard]


commands = Commands()
groupbox_bar = bar.Bar(
    [
        widget.Spacer(),
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


keys = [
    # A list of available commands that can be bound to keys can be found
    # at https://docs.qtile.org/en/latest/manual/config/lazy.html
    # Switch between windows
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(),
        desc="Move window focus to other window"),
    # Move windows between left/right columns or move up/down in current stack.
    # Moving out of range in Columns layout will create new column.
    Key(
        [mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"
    ),
    Key(
        [mod, "shift"],
        "l",
        lazy.layout.shuffle_right(),
        desc="Move window to the right",
    ),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    # Grow windows. If current window is on the edge of screen and direction
    # will be to screen edge - window would shrink.
    Key([mod, "control"], "h", lazy.layout.grow_left(),
        desc="Grow window to the left"),
    Key(
        [mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"
    ),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    # Toggle between split and unsplit sides of stack.
    # Split = all windows displayed
    # Unsplit = 1 window displayed, like Max layout, but still with
    # multiple stack panes
    Key(
        [mod, "shift"],
        "Return",
        lazy.layout.toggle_split(),
        desc="Toggle between split and unsplit sides of stack",
    ),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    # Toggle between different layouts as defined below
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod, "shift"], "c", lazy.window.kill(), desc="Kill focused window"),
    Key(
        [mod],
        "f",
        lazy.window.toggle_fullscreen(),
        desc="Toggle fullscreen on the focused window",
    ),
    Key(
        [mod],
        "t",
        lazy.window.toggle_floating(),
        desc="Toggle floating on the focused window",
    ),
    Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    # my keybindings launch programs
    Key([mod], "p", lazy.spawn("rofi -show drun"), desc="Launch rofi"),
    Key(
        [mod],
        "c",
        lazy.spawn("google-chrome-stable"),
        desc="Launch google-chrome-stable",
    ),
    Key([mod], "b", lazy.hide_show_bar("top"),
        desc="Toggle the top bar on/off"),
    Key(
        [mod, "shift"],
        "s",
        lazy.widget["widgetbox1"].toggle(),
        desc="Toggle widgetbox with systray",
    ),
    Key(
        [mod, "shift"],
        "d",
        lazy.widget["widgetbox2"].toggle(),
        desc="Toggle widgetbox with clock",
    ),
]

# Add key bindings to switch VTs in Wayland.
# We can't check qtile.core.name in default config as it is loaded before qtile is started
# We therefore defer the check until the key binding is run by using .when(func=...)
for vt in range(1, 8):
    keys.append(
        Key(
            ["control", "mod1"],
            f"f{vt}",
            lazy.core.change_vt(vt).when(
                func=lambda: qtile.core.name == "wayland"),
            desc=f"Switch to VT{vt}",
        )
    )


for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc=f"Switch to group {i.name}",
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc=f"Switch to & move focused window to group {i.name}",
            ),
            # Or, use below if you prefer not to switch to that group.
            # # mod + shift + group number = move focused window to group
            # Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
            #     desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_focus="#89b4fa",
        border_focus_stack=["#d75f5f", "#8f3d3d"],
        border_width=4,
    ),
    layout.Max(),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadTall(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

widget_defaults = dict(
    font="Fira code",
    fontsize=24,
    padding=3,
)
extension_defaults = widget_defaults.copy()

logo = os.path.join(os.path.dirname(libqtile.resources.__file__), "logo.png")

wallpapers = {
    "1": "/home/vadim/.config/wallpaper/gori_vershina_sumerki.jpg",
    "2": "/home/vadim/.config/wallpaper/archlinux.png",
    "3": "/home/vadim/.config/wallpaper/wall.png",
    "4": "/home/vadim/.config/wallpaper/autumn-forest-wallpaper.1920x1080.jpg",
    "5": "/home/vadim/.config/wallpaper/gory_tuchi_more_69213_1920x1080.jpg",
    "6": "/home/vadim/.config/wallpaper/sunset.jpeg",
    "7": "/home/vadim/.config/wallpaper/dark-cat-rosewater.png",
}


@hook.subscribe.setgroup
def set_wallpaper():
    # """Эта функция вызывается при каждой смене группы"""
    group_name = qtile.current_group.name
    # Получаем путь к обоям из словаря. .get() безопаснее, чем [],
    # так как он не вызовет ошибку, если для группы нет обоев.
    wallpaper_path = wallpapers.get(group_name)

    if wallpaper_path and os.path.exists(wallpaper_path):
        # Используем subprocess.Popen, чтобы команда не блокировала Qtile.
        # feh --bg-scale масштабирует изображение по размеру экрана.
        subprocess.Popen(["feh", "--bg-scale", wallpaper_path])


# --- Конец блока кода ---


# Этот хук установит обои при первом запуске Qtile


@hook.subscribe.startup_once
def new_wallpaper():
    subprocess.Popen(["picom", "-b"])
    subprocess.Popen(
        ["setxkbmap", "-layout", "us,ru", "-option",
            "grp:caps_toggle,grp_led:scroll"]
    )
    # Вызываем нашу функцию, чтобы установить обои для первой группы
    set_wallpaper()


screens = [
    Screen(top=groupbox_bar),
]

# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)
auto_fullscreen = True
focus_on_window_activation = "smart"
focus_previous_on_window_remove = False
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# xcursor theme (string or None) and size (integer) for Wayland backend
wl_xcursor_theme = None
wl_xcursor_size = 24

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
