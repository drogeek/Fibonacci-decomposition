from utils import app, conn
from fib_decomp import fib_decompose, FunctionCache
from db import find_max_value
import json


@app.route('/fib/<int:n>', methods=['GET'])
def fib_decompose_exposed(n):
    #create the cache that will call fib_decompose if the value for n doesn't exist in the database yet
    cache = FunctionCache(lambda x: fib_decompose(x, cache), conn)
    return json.dumps(tuple(cache.get(n))), 200

@app.route('/')
def hello():
    return "hello", 200

# let's decide that the health of the service is the max value of the precomputed decomposition, since those that are under it should also be precomputed
@app.route('/health', methods=['GET'])
def get_service_health():
    max_value = find_max_value(conn) 
    if max_value:
        return str(max_value[0]), 200
    else:
        return "0", 200

