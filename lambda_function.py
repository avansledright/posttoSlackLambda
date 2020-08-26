import logging
logging.basicConfig(level=logging.DEBUG)

import os
from slack import WebClient
from slack.errors import SlackApiError

def lambda_handler():
    slack_token = os.environ["slackBot"]
    client = WebClient(token=slack_token)    
    try:
        response = client.chat_postMessage(
            channel="####################",
            text="A file has been uploaded"
        )

    except SlackApiError as e:
        assert e.response["error"]
    return 