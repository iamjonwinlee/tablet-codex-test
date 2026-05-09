from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello from Android Tablet Python Workstation'


if __name__ == '__main__':
    # Listen only on localhost for Termux local access
    app.run(host='127.0.0.1', port=8508)
