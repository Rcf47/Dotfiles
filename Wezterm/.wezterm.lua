local wezterm = require 'wezterm'

local config = {}

if wezterm.config_builder then
  config = wezterm.config_builder()
end

config.color_scheme = "Catppuccin Mocha"
config.window_background_opacity = .88
config.font_size = 22

config.colors = {
  tab_bar = {
    active_tab = {
      bg_color = '#414868',
      fg_color = '#fefefe',
    },
    inactive_tab = {
      bg_color = '#1a1b26',
      fg_color = '#808080',
    },
    new_tab = {
      bg_color = '#1a1b26',
      fg_color = '#fefefe',
    },
    inactive_tab_edge = '#1a1b26',
  },
  background = 'black'
}
return config
