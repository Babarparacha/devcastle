# ============================================================================
# THE CLIENT (Simulating a user talking to our API)
# ============================================================================
import requests

# 1. Test the GET Request (Checking if Hexora is online)
print("--- Testing /status ---")
response = requests.get('http://127.0.0.1:5000/status')
# print(response.json())

# print("\n--- Testing /predict-load ---")
# # 2. Test the POST Request (Sending a massive traffic spike to the AI)
# # We pack our data into a Python dictionary (which becomes JSON)
payload = {
    "api_requests": 4.5  # Sending 450 requests per second
}

# # We POST the payload to the URL
ml_response = requests.post('http://127.0.0.1:5000/predict-load', json=payload)

# # Print the AI's final verdict!
print(ml_response.json())