import time
import requests
from datetime import datetime

# Replace with your actual webhook URL and token
WEBHOOK_URL = "https://sensi-webhook.onrender.com/adjust-temp"
BEARER_TOKEN = "sk_7fA9xL2vQpT3zW8rJmK5uE1cXyB0dN6g"

def call_webhook():
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json"
    }
    payload = {}
    response = requests.post(WEBHOOK_URL, json=payload, headers=headers)
    print(f"{datetime.now()} - Status: {response.status_code}, Response: {response.text}")

while True:
    call_webhook()
   
