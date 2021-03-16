from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/print")
def test_print():
    return jsonify({"test":"hello"})

if  __name__ == '__main__':
    app.run(port=5003, debug=True)