from utils import app
from task2 import fib_decompose, FunctionCache
import json
from db import conn

@app.route('/fib/<int:n>', methods=['GET'])
def fib_decompose_exposed(n):
    cache = FunctionCache(lambda x: fib_decompose(x, cache), conn)
    return json.dumps(tuple(cache.get(n))), 200

@app.route('/')
def hello():
    cur = conn.cursor()
    try:
        cur.execute("SELECT * from fib;")
        return json.dumps(cur.fetchall()), 200
    except:
        print("I can't SELECT from fib")
    return "error", 500

average_time = 0
@app.route('/health', methods=['GET'])
def get_service_health():
    pass

