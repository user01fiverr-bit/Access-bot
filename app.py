from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

TOKEN = "8734052042:AAG7N2xYcAqS_uwiW7NWfrHBHFfWa9iNKsc"
CHAT = "7656289635"
API = f"https://api.telegram.org/bot{TOKEN}/"

@app.route('/', methods=['POST'])
def log():
    data = request.json
    text = data.get('text')
    if text:
        requests.post(API + "sendMessage", json={"chat_id": CHAT, "text": text})
    return jsonify(ok=True)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
