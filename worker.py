import os
import time
import requests
from datetime import datetime, timedelta
import pytz

# Load environment variables
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
BEARER_TOKEN = os.getenv("BEARER_TOKEN")

# Timezone setup
eastern = pytz.timezone("US/Eastern")
target_hour = 11
target_minute = 30

def wait_until_next_run():
    now = datetime.now(eastern)
    next_run = now.replace(hour=target_hour, minute=target_minute, second=0, microsecond=0)

    if now >= next_run:
        next_run += timedelta(days=1)

    wait_seconds = (next_run - now).total_seconds()
    print(f"Waiting {int(wait_seconds)} seconds until next run at {next_run.strftime('%Y-%m-%d %H:%M:%S %Z')}")
    time.sleep(wait_seconds)

def call_webhook():
    headers = {
        "Authorization": f"Bearer {BEARER_TOKEN}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.post(WEBHOOK_URL, json={}, headers=headers)
        print(f"{datetime.now(eastern)} - Status: {response.status_code}, Response: {response.text}")
    except Exception as e:
        print(f"Error calling webhook: {e}")

# Main loop
while True:
    #wait_until_next_run()
    call_webhook()
