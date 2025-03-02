from flask import Flask
from prometheus_client import start_http_server, Gauge, Counter

app = Flask(__name__)

# Simple metrics
requests_total = Counter('requests_total', 'Total number of requests')
request_latency = Gauge('request_latency_seconds', 'Request latency in seconds')

@app.route('/')
def hello():
    requests_total.inc()
    start_time = time.time()
    time.sleep(0.1) # Simulate some work. Adjust for longer delays.
    end_time = time.time()
    request_latency.set(end_time - start_time)
    return "Hello, World!"

if __name__ == '__main__':
    start_http_server(9100) # Expose metrics on port 9100
    app.run(debug=True, host='0.0.0.0', port=5000) # Run Flask on port 5000
import time
