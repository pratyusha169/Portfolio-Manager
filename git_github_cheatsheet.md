# Git & GitHub Cheatsheet: Top 25 Commands

A practical guide to the commands you'll use every day.

---

## The Big Picture

Git tracks changes to your code locally. GitHub hosts that code remotely and adds collaboration tools (pull requests, issues, code review). Most of your day-to-day work follows this loop:

```
pull → branch → edit → stage → commit → push → pull request
```

---

## Setup (Do This Once)

| Command | What it does |
|---------|--------------|
| `git config --global user.name "Your Name"` | Set your name for commits |
| `git config --global user.email "you@email.com"` | Set your email for commits |

---

## Starting a Project

| Command | What it does |
|---------|--------------|
| `git init` | Turn the current folder into a git repository |
| `git clone <url>` | Download a repository from GitHub to your machine |

> **Example:** `git clone https://github.com/user/repo.git` creates a local copy of that repo.

---

## The Daily Workflow

These are the commands you'll type dozens of times a day.

| Command | What it does |
|---------|--------------|
| `git status` | Show which files are changed, staged, or untracked |
| `git add <file>` | Stage a specific file for the next commit |
| `git add .` | Stage all changed files at once |
| `git commit -m "message"` | Save staged changes with a descriptive message |
| `git push` | Upload your local commits to GitHub |
| `git pull` | Download and merge the latest changes from GitHub |

> **Tip:** Write commit messages in the imperative mood: `"Fix login bug"` not `"Fixed login bug"`. Future you will thank present you.

---

## Branching

Branches let you work on features or fixes without touching the main codebase until you're ready.

| Command | What it does |
|---------|--------------|
| `git branch` | List all local branches |
| `git branch <name>` | Create a new branch |
| `git checkout <name>` | Switch to a branch |
| `git checkout -b <name>` | Create a new branch and switch to it in one step |
| `git merge <branch>` | Merge another branch into your current one |

> **Tip:** `git checkout -b feature/my-feature` is the command you'll use most — it creates and switches in one shot.

---

## Inspecting History

| Command | What it does |
|---------|--------------|
| `git log` | Show the full commit history |
| `git log --oneline` | Show a compact one-line-per-commit history |
| `git diff` | Show unstaged changes in your working files |
| `git diff --staged` | Show changes that are staged but not yet committed |

> **Tip:** `git log --oneline --graph` draws a visual branch tree in your terminal — useful when things get complex.

---

## Undoing Things

| Command | What it does |
|---------|--------------|
| `git restore <file>` | Discard unstaged changes to a file |
| `git reset HEAD~1` | Undo the last commit, keeping your changes staged |
| `git stash` | Temporarily shelve your uncommitted changes |
| `git stash pop` | Bring stashed changes back |

> **Warning:** `git reset --hard` permanently discards changes. Use `git restore` or `git reset` (without `--hard`) when in doubt.

---

## GitHub-Specific Workflow

These aren't git commands — they're GitHub concepts you'll use constantly.

| Action | How to do it |
|--------|--------------|
| **Fork a repo** | Click "Fork" on GitHub — creates your own copy of someone else's repo |
| **Open a Pull Request** | Push your branch, then click "Compare & pull request" on GitHub |
| **Review a PR** | Go to the PR → "Files changed" → leave inline comments |
| **Merge a PR** | Click "Merge pull request" after approval |

---

## Quick Reference Card

```
SETUP         git config --global user.name / user.email

START         git init                  git clone <url>

DAILY         git status                git add . / <file>
              git commit -m "msg"       git push
              git pull

BRANCH        git branch <name>         git checkout -b <name>
              git checkout <name>       git merge <branch>

HISTORY       git log --oneline         git diff / --staged

UNDO          git restore <file>        git reset HEAD~1
              git stash                 git stash pop

GITHUB        Fork → Branch → PR → Review → Merge
```

---

*Master these 25 and you'll handle 95% of real-world git and GitHub work with confidence.*
