local wk = require("which-key")

wk.register({
      ["<leader>t"] = { name = "+Telescope" },
      ["<leader>g"] = { name = "+Fugitive git" },
      ["<leader>h"] = { name = "+Gitsigns" },
      ["s"] = { name = "+Split window" },
      ["<leader><leader>"] = { name = "+Highlight color" },
      ["<leader>l"] = { name = "+Lazygit" },
})
