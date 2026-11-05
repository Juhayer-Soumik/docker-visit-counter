import os
import redis
from flask import Flask

app = Flask(__name__)
cache = redis.Redis(host=os.getenv("REDIS_HOST", "redis"), port=6379)

@app.route("/")
def index():
    count = cache.incr("visits")
    return f"Hello! This page has been visited {count} times.\n"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
