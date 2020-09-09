import psycopg2
import json

#TODO create a pool of connections instead
try:
    conn=psycopg2.connect("host='db' dbname='postgres' user='postgres' password='titbpembanmih32s'")
except:
    print ("I am unable to connect to the database.")



def insert_into_db(key, value):
    value = json.dumps(value)
    cur = conn.cursor()
    try:
        cur.execute("INSERT INTO fib VALUES ({}, '{}') ON CONFLICT DO NOTHING;".format(key, value))
        conn.commit();
    except:
        print("can't insert into table")

def lookup_table(key):
    cur = conn.cursor()
    try:
        cur.execute("SELECT data FROM fib WHERE id = {}".format(key))
        return cur.fetchone()
    except:
        print("couldn't look into table")

def create_table():
    cur = conn.cursor()
    try:
        cur.execute("CREATE TABLE IF NOT EXISTS fib (id integer, data jsonb);")
        cur.execute("CREATE INDEX IF NOT EXISTS fib_key_idx ON fib USING hash (id) ")
        print("table created")
        conn.commit();
    except:
        print("can't create table")   
