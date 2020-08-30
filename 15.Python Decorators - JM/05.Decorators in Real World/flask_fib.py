from flask import Flask

app = Flask(__name__)


@app.route("/")
def print_fib():
    return "<h1>Fibonacci</h1>"
