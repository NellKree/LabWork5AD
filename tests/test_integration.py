import requests
import unittest

class TestServices(unittest.TestCase):
    def test_data_ingestion(self):
        response = requests.get("http://localhost:5000/data")
        self.assertEqual(response.status_code, 200)

    def test_bot_detection(self):
        response = requests.post(
            "http://localhost:5001/detect",
            json={"data": "bot activity"},
            headers={"Content-Type": "application/json"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["status"], "detected")

    def test_data_visualization(self):
        response = requests.get("http://localhost:5002/visualize")
        self.assertEqual(response.status_code, 200)
        self.assertIn("visualization", response.json())

if __name__ == "__main__":
    unittest.main()