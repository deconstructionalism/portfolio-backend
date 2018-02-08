from flask import Flask, jsonify
app = Flask(__name__)

me = {"hello": 6}

@app.route('/')
def hello():
    return jsonify(me)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)