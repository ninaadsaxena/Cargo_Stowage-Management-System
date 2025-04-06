import sqlite3
from contextlib import closing

DATABASE = 'cargo.db'

def init_db():
    with closing(sqlite3.connect(DATABASE)) as db:
        with open('schema.sql', 'r') as f:
            db.cursor().executescript(f.read())
        db.commit()

def query_db(query, args=(), one=False):
    with closing(sqlite3.connect(DATABASE)) as db:
        db.row_factory = sqlite3.Row
        cur = db.execute(query, args)
        rv = cur.fetchall()
        cur.close()
        return (rv[0] if rv else None) if one else rv

def execute_db(query, args=()):
    with closing(sqlite3.connect(DATABASE)) as db:
        cur = db.execute(query, args)
        db.commit()
        return cur.lastrowid
