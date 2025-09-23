from libqtile.config import Group, Match


myTags = "󰖟  󰌢  󰭹 󰋩 󰒋 "
groups = [
    Group(name="1", label="󰖟 ", spawn="google-chrome-stable"),
    Group(name="2", label=" ", spawn="kitty"),
    Group(name="3", label="󰌢 ", spawn=None),
    Group(name="4", label=" ", spawn="Telegram"),
    Group(name="5", label="󰭹 ", spawn=None),
    Group(name="6", label="󰋩 ", spawn=None),
    Group(name="7", label="󰒋 ", spawn=None),
]
