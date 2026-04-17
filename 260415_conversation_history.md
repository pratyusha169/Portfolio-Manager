# Conversation History — Project Tracker

**Date:** 2026-04-15

---

## Turn 1

**User:**
When I run app.py in `/Users/pratyushahunnewell/Documents/Scripts/NTAI_TOP/project_tracker/app.py`, why do I get a `WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.`?

**Assistant:**
This is normal and expected behavior. The warning comes from Flask's built-in development server, which you're using via `app.run(debug=True)` on line 69.

**Why it appears:** Flask's built-in server (Werkzeug) is intentionally single-threaded, not designed for concurrent requests, and lacks security hardening. Flask prints this warning to remind you not to expose it publicly.

**For local development, this warning is harmless** — you can safely ignore it while building/testing on your own machine.

If you want to suppress it for local use, you have a couple of options:

**Option 1 — Keep using Flask's dev server but silence the warning** (simplest):

You can suppress it by setting the `WERKZEUG_RUN_MAIN` environment variable, but there's no clean built-in flag to silence just that warning without side effects.

**Option 2 — Use a proper WSGI server locally** (recommended even for local use):

Install `waitress` (lightweight, works on Mac/Windows/Linux):

```bash
pip install waitress
```

Then change `app.py` lines 68–69:

```python
if __name__ == '__main__':
    from waitress import serve
    serve(app, host='127.0.0.1', port=5050)
```

No more warning, and it handles concurrent requests better. You'd lose the auto-reloader though — for active development, the Flask dev server with its reloader is still convenient, so just ignoring the warning is fine.

**TL;DR:** The warning is just Flask being cautious. For a local project tracker that only you use, it's safe to ignore it entirely.

---

## Turn 2

**User:**
Export the entire conversation history to a markdown file in the PROJECT_TRACKER folder.

**Assistant:**
Wrote this file: `conversation_history.md` in the project_tracker directory.
