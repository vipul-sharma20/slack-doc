import os
from typing import List

from slack import WebClient

import plugins.utils as utils


class ExportSlackThread:
    """
    Base class for abstract factory
    """

    def __init__(self, message_data: str):
        self.client = WebClient(token=os.environ["SLACK_API_TOKEN"])
        self.message_data = message_data

    def get_thread(self) -> List:
        channel_id = self.message_data["channel"]["id"]
        parent_id = self.message_data["message"]["thread_ts"]

        return utils.get_conversation_history(channel_id, parent_id, self.client)

    def send_message(self, text: str):
        channel = self.message_data["channel"]["name"]
        thread_ts = self.message_data["message"]["thread_ts"]

        self.client.chat_postMessage(
            channel=f"#{channel}", thread_ts=thread_ts, text=f"Doc at: {text}")

    def export_thread(self):
        raise NotImplementedError
