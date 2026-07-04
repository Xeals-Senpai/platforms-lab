from flask import Flask
from prometheus_client import Counter, Info, generate_latest
import time
import random
import os

# Create Flask app and generate metrics
app = Flask(__name__)

requests_counter = Counter(
    "web_requests_total",
    "Total number of requests"
)

app_info = Info(
    "platforms_app",
    "Platform Lab application information"
)

app_info.info({
    "version": "1.0.0"
})

# Define routes
@app.route("/")
def hello():
    requests_counter.inc()
    return "Hello World from Flask with Docker, Ansible and Prometheus!\n"

# Simulates a slow request
@app.route("/slow")
def slow():
    requests_counter.inc()
    time.sleep(10)
    return "Simulating a slow request...\n"

# Simulates random failures
@app.route("/random")
def random_response():
    requests_counter.inc()
    if random.random() < 0.5:
        raise Exception("Random failure occurred!")
    return "No failure this time!\n"

# Simulates a high CPU load
@app.route("/load")
def load():
    requests_counter.inc()
    total = sum(range(10**7))  # Simulates CPU load
    return f"Simulated CPU load total: {total}\n"

# Simulates a crash
@app.route("/crash")
def crash():
    requests_counter.inc()
    os._exit(1)  # Simulate a crash by exiting the process
    return "This will never show, crash initiated!\n"

# Prometheus metrics endpoint
@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; charset=utf-8'}

# Health endpoint
@app.route("/health")
def health():
    requests_counter.inc()
    return {"status": "healthy"}, 200

# Ready endpoint
@app.route("/ready")
def ready():
    requests_counter.inc()
    return {"status": "ready"}, 200

# Version endpoint
@app.route("/version")
def version():
    requests_counter.inc()
    return {"version": "1.0.0"}, 200

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5050)