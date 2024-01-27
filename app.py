from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
import requests
 
 

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large-v3"
HEADERS = {"Authorization": "Bearer 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"}   

@app.route('/')
def home():
    return render_template('index0.html')

@app.route("/transcribe", methods=["POST"])
@cross_origin()  # This will enable CORS for the /transcribe route
def transcribe():
    try:
        data = request.data
        response = requests.post(API_URL, headers=HEADERS, data=data)
        result = response.json()
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(port=5000, debug=True)
