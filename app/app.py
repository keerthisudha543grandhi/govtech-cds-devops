from flask import Flask
import redis
import os

app = Flask(__name__)

REDIS_HOST = os.getenv("REDIS_HOST", "localhost")
redis_client = redis.Redis(host=REDIS_HOST, port=6379, decode_responses=True)

@app.route("/")
def home():
    count = redis_client.incr("visitor_count")
    return f"This is the {count} visitor"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
