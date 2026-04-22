# Vim Cheatsheet: Top 25 Commands

A practical guide to the commands you'll use every day.

---

## Getting In and Out

Vim is a *modal* editor — your keystrokes mean different things depending on which mode you're in.
The three modes you need to know: **Normal** (navigation), **Insert** (typing), and **Command** (`:` commands).

| Command | What it does |
|---------|--------------|
| `vim filename` | Open a file in vim |
| `i` | Enter Insert mode (start typing before cursor) |
| `Esc` | Return to Normal mode |
| `:w` | Save (write) the file |
| `:q` | Quit |
| `:wq` or `ZZ` | Save and quit |
| `:q!` | Quit without saving (force) |

> **Tip:** If you're ever stuck, press `Esc` a couple of times to get back to Normal mode, then proceed.

---

## Moving Around (Normal Mode)

These are your bread-and-butter navigation commands. Learn these first.

| Command | What it does |
|---------|--------------|
| `h j k l` | Move left / down / up / right |
| `w` | Jump forward one word |
| `b` | Jump back one word |
| `0` | Jump to the beginning of the line |
| `$` | Jump to the end of the line |
| `gg` | Jump to the top of the file |
| `G` | Jump to the bottom of the file |
| `Ctrl-d` | Scroll down half a page |
| `Ctrl-u` | Scroll up half a page |

> **Tip:** Prefix any motion with a number to repeat it. `5j` moves down 5 lines. `3w` jumps forward 3 words.

---

## Editing Text (Normal Mode)

You don't always need Insert mode to make changes. These commands let you edit without switching modes.

| Command | What it does |
|---------|--------------|
| `x` | Delete the character under the cursor |
| `dd` | Delete (cut) the entire current line |
| `yy` | Yank (copy) the entire current line |
| `p` | Paste after the cursor |
| `u` | Undo the last change |
| `Ctrl-r` | Redo (undo an undo) |
| `o` | Open a new line below and enter Insert mode |
| `A` | Append to the end of the current line (enters Insert mode) |

---

## Searching and Replacing

| Command | What it does |
|---------|--------------|
| `/word` | Search forward for `word` |
| `n` | Jump to the next match |
| `N` | Jump to the previous match |
| `:%s/old/new/g` | Replace all occurrences of `old` with `new` in the file |

> **Example:** `:%s/foo/bar/g` replaces every instance of `foo` with `bar`. Add `c` at the end (`:%s/foo/bar/gc`) to confirm each replacement.

---

## Quick Reference Card

```
MODES         i → Insert   Esc → Normal   : → Command

MOVE          h←  j↓  k↑  l→    w(word)  b(back)
              0(line start)  $(line end)  gg(top)  G(bottom)

EDIT          x(del char)  dd(del line)  yy(copy)  p(paste)
              u(undo)  Ctrl-r(redo)  o(new line)  A(append)

SEARCH        /word  →  n(next)  N(prev)
REPLACE       :%s/old/new/g

SAVE/QUIT     :w  :q  :wq  :q!
```

---

*That's it. Master these 25 and you'll be productive in vim within a day.*
