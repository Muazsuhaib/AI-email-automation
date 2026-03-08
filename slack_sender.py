import requests
import os

SLACK_WEBHOOK = os.getenv("SLACK_WEBHOOK")


def send_to_slack(message):

    payload = {
        "text": message
    }

    requests.post(SLACK_WEBHOOK, json=payload)
