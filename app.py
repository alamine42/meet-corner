from __future__ import print_function
from flask import Flask, render_template, request, session, \
flash, redirect, url_for, g
import sqlite3
from flask_debugtoolbar import DebugToolbarExtension
from functools import wraps

DATABASE_PATH = 'meet_corner.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'Hacker5b3weighliftin9'
DEBUG_TB_INTERCEPT_REDIRECTS = True

app = Flask('__name__')

app.config.from_object(__name__)

app.debug = True

toolbar = DebugToolbarExtension(app)

def connect_db():
    return sqlite3.connect(app.config['DATABASE_PATH'])


def login_required(test):
    @wraps(test)
    def wrap(*args, **kwargs):
        if 'logged_in' in session:
            return test(*args, **kwargs)
        else:
            flash('You need to login first.')
            return redirect(url_for('login'))
    return wrap


@app.route('/')
@app.route('/calendar')
def calendar_view():
    g.db = connect_db()
    cur = g.db.execute("SELECT * FROM meets")

    meets = [dict(
        location = row[3], 
        meet_type = row[9], 
        contact_email = row[5], 
        start_date = row[7], 
        end_date = row[8]
        ) for row in cur.fetchall()]

    g.db.close()

    return render_template('calendar.html', meets = meets)

@app.route('/meet/<int:meet_id>/')
def view_meet(meet_id):
    if meet_id > 0:
        return render_template('view_meet.html')
    else:
        return 'What you talking bout, Willis?', 404


@app.route('/new_meet')
@login_required
def new_meet():
    return render_template('new_meet.html')

@app.route('/add_meet', methods = ['POST'])
def add_meet():

    print(request.form)
    meet_name = request.form['meet_name']
    meet_location = request.form['meet_location']
    meet_address = request.form['meet_address']
    meet_contact_email = request.form['meet_contact_email']
    meet_event_link = request.form['meet_event_link']
    meet_start_date = request.form['meet_start_date']
    meet_end_date = request.form['meet_end_date']
    meet_type = request.form['meet_type']

    if not meet_name or not meet_location or not meet_contact_email or not meet_start_date or not meet_end_date or not meet_type:
        flash('Please fill out all the required fields.')
        return redirect(url_for('new_meet'))
    else:
        if not meet_address:
            meet_address = ''
        if not meet_event_link:
            meet_event_link = ''

        g.db = connect_db()
        g.db.execute('INSERT INTO meets \
            (username, meet_name, location, address, contact_email, event_link, start_date, end_date, meet_type) \
            values (?, ?, ?, ?, ?, ?, ?, ?, ?)',
            ['admin', meet_name, meet_location, meet_address, meet_contact_email, meet_event_link, meet_start_date, meet_end_date, meet_type])
        g.db.commit()
        g.db.close()

        flash('New meet successfully created!')

        return redirect(url_for('calendar_view'))

@app.route('/login', methods = ['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME'] or \
            request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid credentials. Please try again.'
        else:
            session['logged_in'] = True
            return redirect(url_for('new_meet'))
        
    return render_template('login.html', error=error)

@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out.')
    return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(port = 5001)