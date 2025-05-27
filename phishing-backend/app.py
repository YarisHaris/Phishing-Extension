from flask import Flask, request, jsonify
from dotenv import load_dotenv
from utils.safe_browsing import check_url_safe
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # enable CORS for all routes


load_dotenv()
app = Flask(__name__)

@app.route("/check_url", methods=["POST"])
def check_url():
    data = request.json
    url = data.get("url")

    if not url:
        return jsonify({"error": "URL is required"}), 400

    is_phishing = check_url_safe(url)
    return jsonify({"phishing": is_phishing})

if __name__ == "__main__":
    app.run(debug=True)
