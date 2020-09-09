from flask import Flask
from flask_caching import Cache
import psycopg2

config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_DIR": "cache",
    "CACHE_TYPE": "filesystem", # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300,
    #"CACHE_MEMCACHED_SERVERS": ("localhost",)
}

app = Flask(__name__)
app.config.from_mapping(config)
cache = Cache(app)

#TODO create a pool of connections instead
try:
    conn=psycopg2.connect("host='db' dbname='postgres' user='postgres' password='titbpembanmih32s'")
except:
    print ("I am unable to connect to the database.")
