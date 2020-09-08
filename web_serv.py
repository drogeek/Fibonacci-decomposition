from flask import Flask
from flask_caching import Cache
import json
from task2 import get_fib_seq 
import itertools as it
from itertools import chain, takewhile
import time

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

@app.route('/')
def hello():
    print("hello")

@app.route('/fib/<int:n>', methods=['GET'])
def fib_decompose_exposed(n):
    return json.dumps(tuple(fib_decompose(n))), 200

average_time = 0
@app.route('/health', methods=['GET'])
def get_service_health():
    pass

@cache.memoize(timeout=1000)
def fib_decompose(n):
    result = set()

    if n <= 3:
        result.add((n,))
    else:
        for fib_nbr in get_fib_seq(n):
            remain = n - fib_nbr 

            # skip solutions that require 1
            if remain < 2 :
                continue

            # get decompositions of the cached remain, computing it if it's not already in the cache
            decompositions = fib_decompose(remain)

            # add fib_nbr to the decompositions of the remaining, then sort each decompositions (to guarantee unicity), 
            # and add the decompositions to the final result if it's not already present
            for decomp in \
                map(
                    lambda x : tuple(sorted((x[0], *x[1]))), 
                    it.product([fib_nbr], decompositions)
                ):
                result.add(decomp)
    return result

@cache.memoize(timeout=1000)
def get_fib_seq(nbr, last_two=(1,2)):
    return tuple(get_fib_seq_gen(nbr, last_two))

def get_fib_seq_gen(nbr, last_two=(1,2)):
    prev, curr = last_two 
    while curr < nbr:
        yield curr 
        tmp = curr
        curr += prev 
        prev = tmp 

if __name__ == "__main__":
    app.run(host='127.0.0.1:5000', threaded=True)
