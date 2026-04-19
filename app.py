from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "hello from kunal (hi all)"

if __name__ == "__mai__":
    app.run(host='0.0.0.0', port=5000)

