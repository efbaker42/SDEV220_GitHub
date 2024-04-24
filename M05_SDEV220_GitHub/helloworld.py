"""Elizabeth Baker
SDEV 220 35N
20APR2024
Case Study Assignment"""

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')