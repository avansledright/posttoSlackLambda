import logging
logging.basicConfig(level=logging.DEBUG)
import requests
import boto3
import os
from urllib.parse import unquote_plus
from slack import WebClient
from slack.errors import SlackApiError

def lambda_handler(event, lambda_context):

    slack_token = os.environ["slackBot"]
    client = WebClient(token=slack_token)
    
    try:
        for record in event['Records']:
            key = unquote_plus(record['s3']['object']['key'])
            response_string = f"The file: {key} has been uploaded"
            response = client.chat_postMessage(
                channel="##################",  # Replace this with your Channel ID
                text="A File was uploaded",    # This is the notification text
                blocks = [{"type": "section", "text": {"type": "plain_text", "text": response_string }}]
        )
    except SlackApiError as e:
        assert e.response["error"]