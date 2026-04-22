# GitHub Collaborator Cheatsheet
**Repo:** `https://github.com/pratyusha169/Portfolio-Manager.git`
**Date Created:** 2026-04-16

---

## 1. Connect Local Repo to Remote Origin

After running `git init` locally, link the repo to GitHub:

```bash
git remote add origin https://github.com/pratyusha169/Portfolio-Manager.git
```

Verify the remote was added:

```bash
git remote -v
```

Expected output:
```
origin  https://github.com/pratyusha169/Portfolio-Manager.git (fetch)
origin  https://github.com/pratyusha169/Portfolio-Manager.git (push)
```

---

## 2. Stage and Commit Your Initial Files

```bash
# Stage all files in the project folder
git add .

# Commit with an initial message
git commit -m "chore(init): initial commit"
```

---

## 3. Set the Default Branch to `main` (if not already set)

```bash
git branch -M main
```

---

## 4. Push to Remote for the First Time

```bash
git push -u origin main
```

The `-u` flag sets `origin/main` as the upstream tracking branch.
All future pushes on this branch can then use just: `git push`

---

## 5. Authentication

GitHub no longer accepts passwords over HTTPS. Use one of the following:

### Option A — Personal Access Token (PAT)
1. Go to GitHub → Settings → Developer Settings → Personal Access Tokens → Tokens (classic)
2. Generate a token with `repo` scope
3. When prompted for a password in the terminal, paste the PAT

### Option B — GitHub CLI (recommended for Windows)
```bash
gh auth login
```
Follow the prompts to authenticate via browser.

### Option C — Git Credential Manager (bundled with Git for Windows)
If you installed Git for Windows, Git Credential Manager handles auth automatically on first push via a browser pop-up.

---

## 6. Everyday Workflow

```bash
# Check status of working directory
git status

# Stage specific file(s)
git add <filename>

# Stage everything
git add .

# Commit staged changes
git commit -m "type(scope): description"

# Push to remote
git push

# Pull latest changes from remote
git pull
```

---

## 7. Collaborator Setup (for teammates added to the repo)

```bash
# Clone the repo (first time only)
git clone https://github.com/pratyusha169/Portfolio-Manager.git

# Navigate into the folder
cd Portfolio-Manager

# Create a feature branch before making changes
git checkout -b feature/your-feature-name

# Push your branch and open a PR
git push -u origin feature/your-feature-name
```

---

## 8. Useful Commands

| Command | Description |
|---|---|
| `git log --oneline` | Compact commit history |
| `git diff` | Show unstaged changes |
| `git diff --staged` | Show staged changes |
| `git stash` | Temporarily shelve uncommitted work |
| `git stash pop` | Restore stashed work |
| `git branch -a` | List all branches (local + remote) |
| `git fetch origin` | Download remote changes without merging |
| `git reset --soft HEAD~1` | Undo last commit, keep changes staged |

---

## 9. .gitignore Reminder

Create a `.gitignore` before your first push to exclude files you don't want tracked:

```bash
# Example entries for a Python/Node project
__pycache__/
*.pyc
.env
node_modules/
.DS_Store
*.docx
```

Add and commit it:
```bash
git add .gitignore
git commit -m "chore: add .gitignore"
git push
```

---

## Quick-Start Summary (copy-paste sequence)

```bash
git remote add origin https://github.com/pratyusha169/Portfolio-Manager.git
git branch -M main
git add .
git commit -m "chore(init): initial commit"
git push -u origin main
```
