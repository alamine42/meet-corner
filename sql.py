import os, logging
import sqlite3

db_filename = 'meet_corner.db'
schema_filename = 'meet_corner_schema.sql'

db_is_new = not os.path.exists(db_filename)

# Open a connection and create the db if it doesn't already exist.

with sqlite3.connect(db_filename) as conn:
    if db_is_new:
        with open(schema_filename, 'rt') as f:
            schema = f.read()
        conn.executescript(schema)

        conn.execute("""
        insert into meet_type (type)
        values ('USAW')
        """)
        
        conn.execute("""
        insert into meet_type (type)
        values ('Mock')
        """)

        conn.execute("""
        insert into meet_type (type)
        values ('Other')
        """)

        conn.execute("""
        insert into meets (location, address, contact_email, event_link, start_date, end_date, meet_type)
        values ('Crossfit South Arlington', '', 'training@epsilonfit.com', 'www.epsilonfit.com', '2015-08-15', '2015-08-16', 'USAW')
        """)