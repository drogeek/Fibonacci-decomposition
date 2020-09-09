from utils import app, conn
from fib_decomp import fib_decompose, FunctionCache
import json


@app.route('/fib/<int:n>', methods=['GET'])
def fib_decompose_exposed(n):
    #create the cache that will call fib_decompose if the value for n doesn't exist in the database
    cache = FunctionCache(lambda x: fib_decompose(x, cache), conn)
    return json.dumps(tuple(cache.get(n))), 200

@app.route('/')
def hello():
    return "hello", 200

average_time = 0
@app.route('/health', methods=['GET'])
def get_service_health():
    pass

