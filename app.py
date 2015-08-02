from __future__ import print_function
from flask import Flask

app = Flask('__name__')
app.config['DEBUG'] = True

@app.route('/')
def landing_page():
    return 'This is a test of the emergency broadcast system.'

if __name__ == '__main__':
    app.run(port = 5001)