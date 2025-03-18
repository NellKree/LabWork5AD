import requests
import unittest

class TestServices(unittest.TestCase):
    def test_data_ingestion(self):
        response = requests.get("http://localhost:5000/data")
        self.assertEqual(response.status_code, 200)

    def test_bot_detection(self):
        response = requests.post("http://localhost:5001/detect", json={"data": "bot activity"})
        self.assertEqual(response.json()["status"], "detected")

if __name__ == "__main__":
    unittest.main()