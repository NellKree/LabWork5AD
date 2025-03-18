from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/data', methods=['GET'])
def fetch_data():
    return jsonify({"status": "success", "data": "sample_data"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)  # Слушаем все интерфейсы на порту 5000