local wezterm = require("wezterm")
local act = wezterm.action
local config = {}

if wezterm.config_builder then
  config = wezterm.config_builder()
end

config.window_decorations = "RESIZE"
config.window_padding = {
  left = 5,
  right = 5,
  top = 5,
  bottom = 5,
}
config.color_scheme = "Catppuccin Mocha"
config.window_background_opacity = 0.88
config.font = wezterm.font("hack nerd font")
config.font_size = 22

config.colors = {
  tab_bar = {
    active_tab = {
      bg_color = "#89B4FA",
      fg_color = "#1e1e2e",
    },
    inactive_tab = {
      bg_color = "#1e1e2e",
      fg_color = "#808080",
    },
    new_tab = {
      bg_color = "#1a1b26",
      fg_color = "#fefefe",
    },
    inactive_tab_edge = "#1a1b26",
  },
  background = "black",
}
config.default_prog = { "/usr/bin/zsh" }

config.leader = { key = "a", mods = "CTRL", timeout_milliseconds = 1500 }
config.keys = {
  {
    key = "!",
    mods = "LEADER | SHIFT",
    action = wezterm.action_callback(function(win, pane)
      local tab, window = pane:move_to_new_window()
    end),
  },
  {
    key = "E",
    mods = "CTRL|SHIFT",
    action = act.PromptInputLine({
      description = "Enter new name for tab",
      action = wezterm.action_callback(function(window, pane, line)
        -- line will be `nil` if they hit escape without entering anything
        -- An empty string if they just hit enter
        -- Or the actual line of text they wrote
        if line then
          window:active_tab():set_title(line)
        end
      end),
    }),
  },
}
return config
