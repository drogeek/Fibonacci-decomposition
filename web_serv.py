from utils import app, conn
import requests
import db

db.create_table(conn)

if __name__ == "__main__":
    app.run(host='127.0.0.1:5000', threaded=True)
