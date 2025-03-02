# app.py
from flask import Flask
from prometheus_client import start_http_server, Summary, Counter

app = Flask(__name__)

# Create a metric to track time spent and requests made.
REQUEST_TIME = Summary('request_processing_seconds', 'Time spent processing request')
REQUEST_COUNT = Counter('request_count', 'Total request count')

@app.route('/')
@REQUEST_TIME.time()
def hello():
    REQUEST_COUNT.inc()
    return "Hello, World!"

if __name__ == '__main__':
    # Start up the server to expose the metrics.
    start_http_server(8000)
    # Run the Flask app.
    app.run(host='0.0.0.0', port=5000)