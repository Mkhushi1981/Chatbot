import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from chat import get_response

app = Flask(__name__, static_folder="static", template_folder="templates")
CORS(app)

@app.get("/")
def index():
    return render_template("index.html")

@app.post("/predict")
def predict():
    data = request.get_json()
    text = data.get("message", "")
    response = get_response(text)
    return jsonify({"answer": response})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=False)
