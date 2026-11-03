import requests

BASE_URL = "http://127.0.0.1:8000"


# Test 1: GET /
def test_home():
    response = requests.get(f"{BASE_URL}/")

    print("\n--- Test GET / ---")
    print("Status code:", response.status_code)
    print("Response:", response.json())


# Test 2: GET /health
def test_health():
    response = requests.get(f"{BASE_URL}/health")

    print("\n--- Test GET /health ---")
    print("Status code:", response.status_code)
    print("Response:", response.json())


# Test 3: POST /predict with valid text
def test_predict():
    data = {
        "text": (
            "Artificial intelligence is transforming many industries. "
            "In healthcare, AI systems help doctors analyze medical "
            "images and detect diseases earlier. "
            "In education, AI-powered tools provide personalized "
            "learning experiences."
        )
    }

    response = requests.post(
        f"{BASE_URL}/predict",
        json=data
    )

    print("\n--- Test POST /predict ---")
    print("Status code:", response.status_code)
    print("Response:", response.json())


# Test 4: POST /predict with invalid text
def test_invalid_input():
    data = {
        "text": "   "
    }

    response = requests.post(
        f"{BASE_URL}/predict",
        json=data
    )

    print("\nTest Invalid Input")
    print("Status code:", response.status_code)
    print("Response:", response.json())


if __name__ == "__main__":
    test_home()
    test_health()
    test_predict()
    test_invalid_input()
