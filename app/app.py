from flask import Flask, request
from prometheus_client import Counter, Info, Histogram, generate_latest
import time
import random
import os

# Create Flask app and generate metrics
app = Flask(__name__)

requests_counter = Counter(
    "web_requests_total",
    "Total number of requests"
)

request_latency = Histogram(
    "web_request_duration_seconds",
    "Time spent processing requests"
)

error_counter = Counter(
    "web_errors_total",
    "Total number of application errors"
)

app_info = Info(
    "platforms_app",
    "Platform Lab application information"
)

app_info.info({
    "version": "1.1.0"
})

# Define routes
@app.route("/")
def hello():
    return "Hello World from Flask with Docker, Ansible and Prometheus!\n"

# Simulates a slow request
@app.route("/slow")
def slow():
    time.sleep(10)
    return "Simulating a slow request...\n"

# Simulates random failures
@app.route("/random")
def random_response():
    if random.random() < 0.5:
        error_counter.inc()
        raise Exception("Random failure occurred!")

    return "No failure this time!\n"

# Simulates a high CPU load
@app.route("/load")
def load():
    total = sum(range(10**7))  # Simulates CPU load
    return f"Simulated CPU load total: {total}\n"

# Simulates a crash
@app.route("/crash")
def crash():
    error_counter.inc()
    os._exit(1)  # Simulate a crash by exiting the process
    return "This will never show, crash initiated!\n"

# Prometheus metrics endpoint
@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': 'text/plain; charset=utf-8'}

# Health endpoint
@app.route("/health")
def health():
    return {"status": "healthy"}, 200

# Ready endpoint
@app.route("/ready")
def ready():
    return {"status": "ready"}, 200

# Version endpoint
@app.route("/version")
def version():
    return {"version": "1.1.0"}, 200

@app.before_request
def start_timer():
    request.start_time = time.time()

@app.after_request
def record_request_metrics(response):
    if request.path != "/metrics":
        requests_counter.inc()
        request_latency.observe(time.time() - request.start_time)

    return response

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)