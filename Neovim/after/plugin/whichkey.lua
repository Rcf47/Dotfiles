local wk = require("which-key")

wk.register({
  ["<leader>t"] = { name = "Telescope" },
  ["<leader>g"] = { name = "Fugitive git" },
  ["<leader>h"] = { name = "Gitsigns" },
  ["<leader>s"] = { name = "Split window" },
  ["<leader><leader>"] = { name = "Highlight color and others" },
  ["<leader>l"] = { name = "Lazygit" },
  ["<leader>d"] = { name = "Diffview" },
  ["<leader>e"] = { name = "Numeric line" },
  ["<leader>j"] = { name = "Jest" },
  ["<leader>m"] = { name = "Harpoon" },
  ["<leader>n"] = { name = "NvimTree" },
  ["<leader>v"] = { name = "Others" },
  ["<leader>vc"] = { name = "Code action" },
  ["<leader>vp"] = { name = 'Open packer' },
  ["<leader>vr"] = { name = 'Reference and rename' },
  ["<leader>vw"] = { name = 'Workspace Symbol' },
  ["<leader>a"] = { name = 'Autosave toggle' },
})
