import os
import subprocess

from libqtile import qtile, hook
from bar import widget_defaults
from keys import keys, mouse
from layouts import layouts, floating_layout
from wallpapers import wallpapers
from groups import groups
from screens import screens


groups = groups

keys = keys
mouse = mouse

widget_defaults = widget_defaults
screens = screens

layouts = layouts
floating_layout = floating_layout

extension_defaults = widget_defaults.copy()


wallpapers = wallpapers


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
    subprocess.Popen(["greenclip", "daemon"])
    # Вызываем нашу функцию, чтобы установить обои для первой группы
    set_wallpaper()


# Drag floating layouts.

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
focus_previous_on_window_remove = False
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = False

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
