from flask import Flask, request, jsonify
from chatbot import get_response

app = Flask(__name__)

@app.route("/")
def home():
    return "AI Chatbot is Running!"

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    response = get_response(user_message)
    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
