from flask import Flask
from flask_caching import Cache

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

