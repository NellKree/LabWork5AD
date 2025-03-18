# data-ingestion-service/app.py
import requests
from flask import Flask, jsonify

app = Flask(__name__)

BOT_DETECTION_URL = "http://bot-detection:5001/detect"  # Используем имя контейнера из docker-compose


@app.route('/data', methods=['GET'])
def fetch_data():
    data = {"status": "success", "data": "sample_data"}

    # Отправляем данные в bot-detection-service
    try:
        response = requests.post(BOT_DETECTION_URL, json={"data": data["data"]},
                                 headers={"Content-Type": "application/json"})
        if response.status_code == 200:
            result = response.json()
            print(f"Bot detection result: {result}")
            data["bot_detection_result"] = result
        else:
            print(f"Error in bot detection: {response.status_code}")
    except Exception as e:
        print(f"Failed to send data to bot-detection-service: {e}")

    return jsonify(data)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)