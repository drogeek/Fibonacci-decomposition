from utils import app
import requests
import db
import json

db.create_table()

if __name__ == "__main__":
    app.run(host='127.0.0.1:5000', threaded=True)
