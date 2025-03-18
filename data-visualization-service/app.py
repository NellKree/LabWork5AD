# data-visualization-service/app.py
import requests
from flask import Flask, jsonify

app = Flask(__name__)

DATA_INGESTION_URL = "http://data-ingestion:5000/data"
BOT_DETECTION_URL = "http://bot-detection:5001/detect"

@app.route('/visualize', methods=['GET'])
def visualize_data():
    try:

        ingestion_response = requests.get(DATA_INGESTION_URL)
        ingestion_data = ingestion_response.json()


        detection_response = requests.post(
            BOT_DETECTION_URL,
            json={"data": ingestion_data["data"]},
            headers={"Content-Type": "application/json"}
        )
        detection_result = detection_response.json()

        visualization_data = {
            "status": "success",
            "ingestion_data": ingestion_data["data"],
            "detection_result": detection_result["status"],
            "visualization": f"Visualization of '{ingestion_data['data']}' with result: {detection_result['status']}"
        }
        return jsonify(visualization_data)
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)