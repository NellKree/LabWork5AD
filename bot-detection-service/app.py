from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/detect', methods=['POST'])
def detect_bots():
    # Проверяем, что данные пришли в формате JSON
    if not request.is_json:
        return jsonify({"error": "Invalid content type"}), 415

    data = request.json.get("data", "")
    if "bot" in data.lower():
        return jsonify({"status": "detected", "reason": "Bot-like activity"})
    return jsonify({"status": "clean"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)