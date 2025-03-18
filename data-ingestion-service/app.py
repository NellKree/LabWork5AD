import time
from datetime import datetime

def fetch_data():
    print(f"[{datetime.now()}] Fetching data from social network...")
    # Здесь можно добавить реальную логику для сбора данных
    return {"status": "success", "data": "sample_data"}

if __name__ == "__main__":
    while True:
        result = fetch_data()
        print(result)
        time.sleep(5)  # Имитация периодического сбора данных