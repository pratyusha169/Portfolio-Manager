### creation date: 2026-04-14

from flask import Flask, render_template, request, redirect, url_for
import csv, json, os

app = Flask(__name__) #creates a Flask application instance.
CSV_FILE  = os.path.join(os.path.dirname(__file__), 'projects.csv')  #gets path of current file, adds projects.csv to it, will be used to tell load_projects where to find csv
DATA_FILE = os.path.join(os.path.dirname(__file__), 'projects.json') #gets path of current file, adds projects.json to it, will be used to tell load_projects where to find json


def load_projects():
    """Read base data from CSV; overlay mutable state from JSON."""
    with open(CSV_FILE, newline='', encoding='utf-8') as f:       #will throw error if file not found.
        projects = [dict(row) for row in csv.DictReader(f)]       #csv.DictReader reads each row as a dict, with keys from the header row of the csv file. Each row is a dict, and the whole thing is an iterable of dicts.
        for p in projects:
            p['id'] = int(p['id']) #converting project id number from string to integer.

    if os.path.exists(DATA_FILE): #check if json file exists
        with open(DATA_FILE) as f:
            overrides = json.load(f) #convert json file to python dict.
        for p in projects:
            ov = overrides.get(str(p['id']), {}) #get override values from json for each project id, if no value exists return empty dict.
            p['status']     = ov.get('status',     p['status']) #get status, github, notes, start and finish dates from override, if none get from csv
            p['github']     = ov.get('github',     p['github'])
            p['notes']      = ov.get('notes',      p['notes'])
            p['start_date'] = ov.get('start_date', '')
            p['finish_date']= ov.get('finish_date','')
            p['phase']      = ov.get('phase',      '')
    else:
        for p in projects:
            p['start_date'] = ''  #if no json file, set start and finish dates to empty strings for all projects.
            p['finish_date'] = ''
            p['phase'] = ''

    return projects


def save_override(pid, status, github, notes, start_date, finish_date, phase):
    """Persist user-editable fields to JSON, keyed by project id."""
    overrides = {}
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE) as f:
            overrides = json.load(f)
    overrides[str(pid)] = {
        'status': status, 'github': github, 'notes': notes,
        'start_date': start_date, 'finish_date': finish_date, 'phase': phase,
    }
    with open(DATA_FILE, 'w') as f:
        json.dump(overrides, f, indent=2) #write the overrides dict to the json file, with indentation for readability.


@app.route('/') 
def index():
    projects = load_projects()
    counts = {s: sum(1 for p in projects if p['status'] == s)
              for s in ['Not Started', 'In Progress', 'Complete', 'Paused']}
    return render_template('index.html', projects=projects, counts=counts)


@app.route('/update/<int:pid>', methods=['POST'])
def update(pid):
    save_override(pid,
                  request.form['status'],
                  request.form.get('github', ''),
                  request.form.get('notes', ''),
                  request.form.get('start_date', ''),
                  request.form.get('finish_date', ''),
                  request.form.get('phase', ''))
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, port=5050)
