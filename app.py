from __future__ import print_function
from flask import Flask, render_template, request, session, \
flash, redirect, url_for, g
import sqlite3

DATABASE = 'meet_corner.db'

app = Flask('__name__')

app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE_PATH'])

@app.route('/')
@app.route('/calendar')
def calendar_view():
    return render_template('calendar.html')

@app.route('/meet/<int:meet_id>/')
def single_meet_view(meet_id):
    if meet_id > 0:
        return render_template('meet.html')
    else:
        return 'What you talking bout, Willis?', 404


if __name__ == '__main__':
    app.run(port = 5001, debug = True)