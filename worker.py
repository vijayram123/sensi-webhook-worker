import os
import requests

# Load secrets from environment variables
webhook_url = os.getenv("WEBHOOK_URL")
bearer_token = os.getenv("BEARER_TOKEN")

# Set headers
headers = {
    "Authorization": f"Bearer {bearer_token}",
    "Content-Type": "application/json"
}

# Send POST request with no payload
response = requests.post(webhook_url, headers=headers)

# Log response
print(f"Status Code: {response.status_code}")
print(f"Response: {response.text}")
