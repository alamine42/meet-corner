import os

basedir = os.path.abspath(os.path.dirname(__file__))

DATABASE = 'meet_corner.db'
USERNAME = 'admin'
PASSWORD = 'admin'
SECRET_KEY = 'Hacker5b3weighliftin9'
DEBUG_TB_INTERCEPT_REDIRECTS = False
WTF_CSRF_ENABLED = True

DATABASE_PATH = os.path.join(basedir, DATABASE)